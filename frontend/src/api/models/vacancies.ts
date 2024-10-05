import { Grade, WorkSchedule } from '@/models/IApplicationsFilter';

export interface Vacancy {
    id: number;
    position: string;
    grade: Grade;
    speciality: string;
    description: string;
    team: string;
    createdAt: string;
}

export interface FetchVacancyColdCandidatesParams {
    vacancyId: number;
}

export interface CreateVacancyParams {
    position: string;
    grade: Grade;
    speciality: string;
    description: string;
    team: string;
    city: string;
    work_format: WorkSchedule;
}

export interface FetchVacancyParams {
    position?: string;
    grade?: Grade;
    speciality?: string;
    city?: string;
    work_format?: WorkSchedule;
}
