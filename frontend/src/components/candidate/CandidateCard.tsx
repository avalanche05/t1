import { Application, ApplicationStatus, Candidate } from '@/api/models';
import { Badge } from '../ui/badge';
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogTrigger } from '../ui/dialog';
import { Button } from '../ui/button';
import { useState } from 'react';
import { Card, CardContent } from '../ui/card';
import { Accordion, AccordionContent, AccordionItem, AccordionTrigger } from '../ui/accordion';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '../ui/select';
import { Textarea } from '../ui/textarea';

type Props = {
    candidate: Candidate;
    application?: Application;
};

const CandidateCard = ({ candidate, application }: Props) => {
    const [status, setStatus] = useState<ApplicationStatus | null>(application?.status ?? null);
    const [vacancy, setVacancy] = useState(candidate.position);
    const [generatedText, setGeneratedText] = useState('');
    const [isStatusDialogOpen, setIsStatusDialogOpen] = useState(false);
    const [isVacancyDialogOpen, setIsVacancyDialogOpen] = useState(false);

    const handleStatusChange = (newStatus: ApplicationStatus) => {
        setStatus(newStatus);
        setIsStatusDialogOpen(false);
        // Here you would typically update the backend with the new status
    };

    const handleVacancyChange = (newVacancy: string) => {
        setVacancy(newVacancy);
        setIsVacancyDialogOpen(false);
    };

    const statusOrder = [
        ApplicationStatus.Pending,
        ApplicationStatus.HrAccepted,
        ApplicationStatus.InterviewerAccepted,
        ApplicationStatus.Offer,
        ApplicationStatus.CandidateAccepted,
    ];

    return (
        <Card className='w-full'>
            <CardContent className='p-6'>
                <div className='flex flex-col md:flex-row gap-6'>
                    <div className='w-full md:w-2/3 space-y-4'>
                        <div className='flex items-center'>
                            <h2 className='text-2xl font-bold'>{candidate.name}</h2>
                            {status && <Badge className='ml-2'>{status}</Badge>}
                        </div>
                        <div className='grid grid-cols-2 gap-4'>
                            <div>
                                <p className='text-sm font-medium'>Телефон:</p>
                                <p>{candidate.phone}</p>
                            </div>
                            <div>
                                <p className='text-sm font-medium'>Электронная почта:</p>
                                <p>{candidate.email}</p>
                            </div>
                            <div>
                                <p className='text-sm font-medium'>Опыт:</p>
                                <p>{candidate.experience} лет</p>
                            </div>
                            <div>
                                <p className='text-sm font-medium'>Класс:</p>
                                <p>{candidate.grade}</p>
                            </div>
                            <div>
                                <p className='text-sm font-medium'>Специальность:</p>
                                <p>{candidate.speciality}</p>
                            </div>
                            <div>
                                <p className='text-sm font-medium'>Образование:</p>
                                <p>{candidate.education}</p>
                            </div>
                        </div>
                        <div>
                            <p className='text-sm font-medium'>Навыки:</p>
                            <div className='flex flex-wrap gap-2 mt-1'>
                                {candidate.skills.map((skill, index) => (
                                    <Badge key={index} variant='secondary'>
                                        {skill}
                                    </Badge>
                                ))}
                            </div>
                        </div>
                        <Accordion type='single' collapsible>
                            <AccordionItem value='summary'>
                                <AccordionTrigger>Краткая информация</AccordionTrigger>
                                <AccordionContent>
                                    {candidate.summary.length > 50
                                        ? `${candidate.summary.substring(0, 50)}...`
                                        : candidate.summary}
                                </AccordionContent>
                            </AccordionItem>
                        </Accordion>
                        <div className='flex items-center space-x-2'>
                            <p className='text-sm font-medium'>Резюме:</p>
                            <a
                                href={candidate.resume_link}
                                target='_blank'
                                rel='noopener noreferrer'
                                className='text-blue-500 hover:underline'
                            >
                                Просмотреть резюме
                            </a>
                        </div>
                    </div>
                    <div className='w-full md:w-1/3 space-y-4'>
                        {application && status && (
                            <div className='space-y-2'>
                                <p className='text-sm font-medium'>Хронология заявки:</p>
                                <div className='relative pt-1'>
                                    <div className='flex mb-2 items-center justify-between'>
                                        {statusOrder.map((step, index) => (
                                            <div key={step} className='text-xs'>
                                                <div
                                                    className={`w-4 h-4 rounded-full ${
                                                        statusOrder.indexOf(status) >= index
                                                            ? 'bg-blue-500'
                                                            : 'bg-gray-300'
                                                    }`}
                                                ></div>
                                                <p className='mt-1'>{step}</p>
                                            </div>
                                        ))}
                                    </div>
                                    <div className='overflow-hidden h-2 mb-4 text-xs flex rounded bg-gray-200'>
                                        <div
                                            style={{
                                                width: `${
                                                    (statusOrder.indexOf(status) /
                                                        (statusOrder.length - 1)) *
                                                    100
                                                }%`,
                                            }}
                                            className='shadow-none flex flex-col text-center whitespace-nowrap text-white justify-center bg-blue-500'
                                        ></div>
                                    </div>
                                </div>
                            </div>
                        )}
                        <div className='flex space-x-2'>
                            <Dialog open={isStatusDialogOpen} onOpenChange={setIsStatusDialogOpen}>
                                <DialogTrigger asChild>
                                    <Button variant='outline'>Изменить статус</Button>
                                </DialogTrigger>
                                <DialogContent>
                                    <DialogHeader>
                                        <DialogTitle>Изменить статус</DialogTitle>
                                    </DialogHeader>
                                    <Select
                                        onValueChange={(value) =>
                                            handleStatusChange(value as ApplicationStatus)
                                        }
                                        defaultValue={status || undefined}
                                    >
                                        <SelectTrigger>
                                            <SelectValue placeholder='Выберите статус' />
                                        </SelectTrigger>
                                        <SelectContent>
                                            {Object.values(ApplicationStatus).map((status) => (
                                                <SelectItem key={status} value={status}>
                                                    {status}
                                                </SelectItem>
                                            ))}
                                        </SelectContent>
                                    </Select>
                                </DialogContent>
                            </Dialog>
                            <Dialog
                                open={isVacancyDialogOpen}
                                onOpenChange={setIsVacancyDialogOpen}
                            >
                                <DialogTrigger asChild>
                                    <Button variant='outline'>Изменить вакансию</Button>
                                </DialogTrigger>
                                <DialogContent>
                                    <DialogHeader>
                                        <DialogTitle>Изменить вакансию</DialogTitle>
                                    </DialogHeader>
                                    <Select
                                        onValueChange={handleVacancyChange}
                                        defaultValue={vacancy}
                                    >
                                        <SelectTrigger>
                                            <SelectValue placeholder='Выберите вакансию' />
                                        </SelectTrigger>
                                        <SelectContent>
                                            <SelectItem value='Программист'>Программист</SelectItem>
                                            <SelectItem value='Менеджер продукта'>
                                                Менеджер продукта
                                            </SelectItem>
                                            <SelectItem value='UX-дизайнер'>UX-дизайнер</SelectItem>
                                        </SelectContent>
                                    </Select>
                                </DialogContent>
                            </Dialog>
                        </div>
                        <div className='space-y-2'>
                            <Button onClick={() => {}} variant='destructive' className='w-full'>
                                Составить текст для отказа
                            </Button>
                            <Button onClick={() => {}} variant='default' className='w-full'>
                                Составить текст для предложения
                            </Button>
                            <Button onClick={() => {}} variant='secondary' className='w-full'>
                                Сгенерировать текст предложения
                            </Button>
                        </div>
                        <Textarea
                            placeholder='Сгенерированный текст появится здесь'
                            value={generatedText}
                            onChange={(e) => setGeneratedText(e.target.value)}
                            rows={4}
                        />
                    </div>
                </div>
            </CardContent>
        </Card>
    );
};

export default CandidateCard;
