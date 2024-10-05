import { Candidate } from './cadidates';
import { Vacancy } from './vacancies';

export enum ApplicationStatuses {
    Pending = 'Pending',
    HrAccepted = 'HrAccepted',
    HrDeclined = 'HrDeclined',
    InterviewerAccepted = 'interviewerAccepted',
    InterviewerDeclined = 'interviewerDeclined',
    Offer = 'offer',
    CandidateAccepted = 'candidateAccepted',
    CandidateDeclined = 'candidateDeclined',
}

export interface Application {
    id: number;
    vacancy: Vacancy;
    candidate: Candidate;
    status: ApplicationStatuses;
    createdAt: string;
}
