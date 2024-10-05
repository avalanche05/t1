import { Candidate } from '@/api/models';
import { CheckCircle2, Clock, XCircle } from 'lucide-react';
import { Badge } from '../ui/badge';
import { Dialog, DialogContent, DialogHeader, DialogTitle, DialogTrigger } from '../ui/dialog';
import { Button } from '../ui/button';
import CandidateDetails from './CandidateDetails';

type Props = {
    candidate: Candidate;
};

const statusOptions = ['Новая', 'Принята', 'Отклонена'];

const CandidateCard = ({ candidate }: Props) => {
    const StatusBadge = ({ status }: { status: string }) => {
        let icon;
        switch (status) {
            case 'Accepted':
                icon = <CheckCircle2 className='w-4 h-4 mr-1' />;
                break;
            case 'Rejected':
                icon = <XCircle className='w-4 h-4 mr-1' />;
                break;
            default:
                icon = <Clock className='w-4 h-4 mr-1' />;
        }

        return (
            <Badge className={`flex items-center bg-blue-100 text-blue-800`}>
                {icon}
                {status}
            </Badge>
        );
    };

    return (
        <div
            key={candidate.id}
            className='mb-4 p-4 border rounded-lg shadow-sm hover:shadow-md transition-shadow'
        >
            <div className='flex justify-between items-start mb-2'>
                <div>
                    <h3 className='font-semibold text-lg'>{candidate.name}</h3>
                    <p className='text-sm text-muted-foreground'>{candidate.position}</p>
                </div>
                <StatusBadge status={status} />
            </div>
            <div className='mt-4 flex justify-between items-center'>
                <select value={status} className='border rounded p-1 text-sm'>
                    {statusOptions.map((option) => (
                        <option key={option} value={option}>
                            {option}
                        </option>
                    ))}
                </select>
                <Dialog>
                    <DialogTrigger asChild>
                        <Button variant='outline' size='sm'>
                            Подробнее
                        </Button>
                    </DialogTrigger>
                    <DialogContent className='max-w-md'>
                        <DialogHeader>
                            <DialogTitle>
                                {candidate.name} - {candidate.position}
                            </DialogTitle>
                        </DialogHeader>
                        <CandidateDetails candidate={candidate} />
                    </DialogContent>
                </Dialog>
            </div>
        </div>
    );
};

export default CandidateCard;
