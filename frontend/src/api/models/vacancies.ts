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
    position?: string | null;
    grade?: Grade | null;
    speciality?: string | null;
    city?: string | null;
    work_format?: WorkSchedule | null;
}
