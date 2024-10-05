import { Candidate } from './candidates';
import { Vacancy } from './vacancies';

export enum ApplicationStatus {
    Pending = 'Pending',
    HrAccepted = 'HrAccepted',
    HrDeclined = 'HrDeclined',
    InterviewerAccepted = 'interviewerAccepted',
    InterviewerDeclined = 'interviewerDeclined',
    Offer = 'offer',
    CandidateAccepted = 'candidateAccepted',
    CandidateDeclined = 'candidateDeclined',
}

export const ApplicationStatusLabels: Record<ApplicationStatus, string> = {
    [ApplicationStatus.Pending]: 'Ожидает обработки',
    [ApplicationStatus.HrAccepted]: 'Принята рекрутером',
    [ApplicationStatus.HrDeclined]: 'Отклонена рекрутером',
    [ApplicationStatus.InterviewerAccepted]: 'Интервью пройдено успешно',
    [ApplicationStatus.InterviewerDeclined]: 'Интервью не пройдено',
    [ApplicationStatus.Offer]: 'Отправлен оффер',
    [ApplicationStatus.CandidateAccepted]: 'Принято кандидатом',
    [ApplicationStatus.CandidateDeclined]: 'Отклонено кандидатом',
};

export interface Application {
    id: number;
    vacancy: Vacancy;
    candidate: Candidate;
    status: ApplicationStatus;
    createdAt: string;
}

export interface FetchApplicationsParams {
    position?: string;
    grade?: string;
    speciality?: string;
    vacancyId?: number;
    status?: ApplicationStatus;
}
