import { ResumeUploadResponse } from '@/api/models';
import ResumeUploadApiService from '@/api/ResumeUploadApiService';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { toast } from '@/components/ui/use-toast';
import { Loader2 } from 'lucide-react';
import { observer } from 'mobx-react-lite';
import { useState } from 'react';

const InterviewFeedback = observer(() => {
    const [uploadResponse, setUploadResponse] = useState<ResumeUploadResponse | null>(null);
    const [isUploading, setIsUploading] = useState(false);
    const [files, setFiles] = useState<File[]>([]);

    const handleFileUpload = (event: React.ChangeEvent<HTMLInputElement>) => {
        const fileList = event.target.files;

        if (fileList) {
            setFiles(Array.from(fileList));
        }
    };

    const uploadFiles = () => {
        setIsUploading(true);

        ResumeUploadApiService.uploadFiles(files, undefined)
            .then((response) => {
                startPolling(response.session_id);
            })
            .catch(() => {
                toast({
                    title: 'Ошибка',
                    description: 'Не удалось загрузить файлы',
                    variant: 'destructive',
                });
            });
    };

    const startPolling = (sessionId: string) => {
        const interval = setInterval(() => {
            ResumeUploadApiService.fetchUploadStatus(sessionId)
                .then((response) => {
                    setUploadResponse(response);

                    if (response.is_finished) {
                        clearInterval(interval);
                        setIsUploading(false);
                    }
                })
                .catch(() => {
                    clearInterval(interval);
                    setIsUploading(false);

                    setUploadResponse((prev) => {
                        if (!prev) {
                            return null;
                        }

                        return {
                            ...prev,
                            error: prev?.error.concat(prev.processing) || [],
                            processing: [],
                        };
                    });

                    toast({
                        title: 'Ошибка',
                        description: 'Не удалось загрузить файлы',
                        variant: 'destructive',
                    });
                });
        }, 5000);
    };

    return (
        <div>
            <h1 className='font-semibold text-lg md:text-2xl mb-4'>Загрузить резюме</h1>

            <p>
                Загрузите файлы с резюме кандидатов, чтобы начать их обработку. Если выбрать
                вакансию, то создастся отклик на эту вакансию.
            </p>

            <div className='mb-4 mt-4'>
                <div className='flex gap-4'>
                    <Input
                        type='file'
                        accept='.pdf'
                        multiple
                        onChange={handleFileUpload}
                        disabled={isUploading}
                        className='mb-2 cursor-pointer w-1/2'
                    />
                </div>

                <Button disabled={isUploading || files.length === 0} onClick={uploadFiles}>
                    {isUploading ? (
                        <>
                            <Loader2 className='mr-2 h-4 w-4 animate-spin' />
                            Загрузка...
                        </>
                    ) : (
                        'Загрузить резюме'
                    )}
                </Button>
            </div>
            <div className='space-y-4'>{uploadResponse && <></>}</div>
        </div>
    );
});

export default InterviewFeedback;
