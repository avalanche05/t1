import { BrainCircuit, Calendar } from 'lucide-react';
import { Card, CardContent, CardHeader, CardTitle } from './ui/card';
import { Vacancy } from '@/api/models';
import { GradeLabels } from '@/models/IApplicationsFilter';

type Props = {
    vacancy: Vacancy;
};

const VacancyCard = ({ vacancy }: Props) => {
    return (
        <Card className='mb-8 bg-slate-200'>
            <CardHeader>
                <CardTitle className='text-sm font-normal text-gray-600'>Вакансия</CardTitle>
                <h2 className='text-2xl font-bold'>
                    {vacancy.position}: {vacancy.speciality}
                </h2>
            </CardHeader>
            <CardContent>
                <div className='flex flex-col md:flex-row gap-8'>
                    <div className='flex flex-col gap-4'>
                        <div className='flex items-center'>
                            <BrainCircuit className='text-purple-600 mr-2' />
                            <span>{GradeLabels[vacancy.grade as keyof typeof GradeLabels]}</span>
                        </div>
                        <div className='flex items-center'>
                            <Calendar className='text-purple-600 mr-2' />
                            <span>3-5 лет</span>
                        </div>
                    </div>

                    <div>
                        <h3 className='font-bold mb-2'>Описание:</h3>
                        <p>{vacancy.description}</p>
                    </div>
                </div>
            </CardContent>
        </Card>
    );
};

export default VacancyCard;
