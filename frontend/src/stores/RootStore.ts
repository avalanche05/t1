import ApplicationsApiService from '@/api/ApplicationsApiService';
import { Application, Candidate } from '@/api/models';
import VacanciesApiService from '@/api/VacanciesApiService';
import { makeAutoObservable } from 'mobx';

export class RootStore {
    applications: Application[] = [];
    isApplicationsLoading = false;

    vacancyColdCandidates: Candidate[] = [];
    isVacancyColdCandidatesLoading = false;

    constructor() {
        makeAutoObservable(this);
    }

    async fetchApplications() {
        this.isApplicationsLoading = true;

        return ApplicationsApiService.fetchApplications({})
            .then((applications) => {
                this.applications = applications;

                return applications;
            })
            .finally(() => {
                this.isApplicationsLoading = false;
            });
    }

    async fetchVacancyColdCandidates(vacancyId: number) {
        this.isVacancyColdCandidatesLoading = true;

        return VacanciesApiService.fetchVacancyColdCandidates({ vacancyId })
            .then((candidates) => {
                this.vacancyColdCandidates = candidates;

                return candidates;
            })
            .finally(() => {
                this.isVacancyColdCandidatesLoading = false;
            });
    }
}
