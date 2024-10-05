'use client';

import { FormEvent, useState } from 'react';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import {
    Select,
    SelectContent,
    SelectItem,
    SelectTrigger,
    SelectValue,
} from '@/components/ui/select';
import { ApplicationStatus, ApplicationStatusLabels } from '@/api/models';
import { Grade, GradeLabels, WorkSchedule, WorkScheduleLabels } from '@/models/IApplicationsFilter';
import { useStores } from '@/hooks/useStores';
import Folders from './Folders';

const ApplicationsFilter = () => {
    const { rootStore } = useStores();

    const [formData, setFormData] = useState({
        name: '',
        city: '',
        position: '',
        speciality: '',
        grade: '',
        experience: '',
        workSchedule: '',
        applicationStatus: '',
    });

    // Обработчик выбора для select полей
    const handleSelectChange = (name: string) => (value: string) => {
        setFormData({ ...formData, [name]: value });
    };

    // Обработчик отправки формы
    const handleSubmit = (e: FormEvent<HTMLFormElement>) => {
        e.preventDefault();

        rootStore.setApplicationFilter({
            name: formData.name || null,
            city: formData.city || null,
            position: formData.position || null,
            speciality: formData.speciality || null,
            grade: (formData.grade as Grade) || null,
            experience: formData.experience || null,
            workSchedule: (formData.workSchedule as WorkSchedule) || null,
            applicationStatus: (formData.applicationStatus as ApplicationStatus) || null,
        });
    };

    return (
        <div className='w-full mx-auto'>
            <Folders />

            <div className='flex flex-col space-y-4 mb-4'>
                <form onSubmit={(e) => handleSubmit(e)} className='flex flex-col space-y-4 mb-4'>
                    <div className='flex space-x-2'>
                        <Input
                            placeholder='Имя'
                            className='flex-1'
                            name='name'
                            value={formData.name}
                            onChange={(e) => setFormData({ ...formData, name: e.target.value })}
                        />

                        <Input
                            placeholder='Город'
                            className='flex-1'
                            name='city'
                            value={formData.city}
                            onChange={(e) => setFormData({ ...formData, city: e.target.value })}
                        />

                        <Select onValueChange={handleSelectChange('position')}>
                            <SelectTrigger className='flex-1'>
                                <SelectValue placeholder='Позиция' />
                            </SelectTrigger>
                            <SelectContent>
                                <SelectItem value='position1'>Позиция 1</SelectItem>
                                <SelectItem value='position2'>Позиция 2</SelectItem>
                                <SelectItem value='position3'>Позиция 3</SelectItem>
                            </SelectContent>
                        </Select>
                    </div>

                    <div className='flex space-x-2'>
                        <Select onValueChange={handleSelectChange('speciality')}>
                            <SelectTrigger className='flex-1'>
                                <SelectValue placeholder='Специальность' />
                            </SelectTrigger>
                            <SelectContent>
                                <SelectItem value='speciality1'>Специальность 1</SelectItem>
                                <SelectItem value='speciality2'>Специальность 2</SelectItem>
                                <SelectItem value='speciality3'>Специальность 3</SelectItem>
                            </SelectContent>
                        </Select>

                        <Select onValueChange={handleSelectChange('grade')}>
                            <SelectTrigger className='flex-1'>
                                <SelectValue placeholder='Грейд' />
                            </SelectTrigger>
                            <SelectContent>
                                {Object.keys(GradeLabels).map((key) => (
                                    <SelectItem key={key} value={key}>
                                        {GradeLabels[key as keyof typeof GradeLabels]}
                                    </SelectItem>
                                ))}
                            </SelectContent>
                        </Select>

                        <Input
                            placeholder='Кол-во лет опыта работы'
                            className='flex-1'
                            name='experience'
                            value={formData.experience}
                            onChange={(e) =>
                                setFormData({ ...formData, experience: e.target.value })
                            }
                        />
                    </div>

                    <div className='flex space-x-2'>
                        <Select onValueChange={handleSelectChange('workSchedule')}>
                            <SelectTrigger className='flex-1'>
                                <SelectValue placeholder='График работы' />
                            </SelectTrigger>
                            <SelectContent>
                                {Object.keys(WorkScheduleLabels).map((key) => (
                                    <SelectItem key={key} value={key}>
                                        {WorkScheduleLabels[key as keyof typeof WorkScheduleLabels]}
                                    </SelectItem>
                                ))}
                            </SelectContent>
                        </Select>

                        <Select onValueChange={handleSelectChange('applicationStatus')}>
                            <SelectTrigger className='flex-1'>
                                <SelectValue placeholder='Статус отклика' />
                            </SelectTrigger>
                            <SelectContent>
                                {Object.keys(ApplicationStatusLabels).map((key) => (
                                    <SelectItem key={key} value={key}>
                                        {
                                            ApplicationStatusLabels[
                                                key as keyof typeof ApplicationStatusLabels
                                            ]
                                        }
                                    </SelectItem>
                                ))}
                            </SelectContent>
                        </Select>

                        <Button className='flex-1' type='submit'>
                            Применить
                        </Button>
                    </div>
                </form>
            </div>
        </div>
    );
};

export default ApplicationsFilter;