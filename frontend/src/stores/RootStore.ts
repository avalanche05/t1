import ApplicationsApiService from '@/api/ApplicationsApiService';
import { Application, Candidate } from '@/api/models';
import VacanciesApiService from '@/api/VacanciesApiService';
import { defaultApplicationsFilter, IApplicationsFilter } from '@/models/IApplicationsFilter';
import { makeAutoObservable } from 'mobx';

export class RootStore {
    applications: Application[] = [];
    isApplicationsLoading = false;
    applicationsFilter: IApplicationsFilter = defaultApplicationsFilter;
    filteredApplications: Application[] = [];

    vacancyColdCandidates: Candidate[] = [];
    isVacancyColdCandidatesLoading = false;

    constructor() {
        makeAutoObservable(this);
    }

    setApplicationFilter(filter: IApplicationsFilter) {
        this.applicationsFilter = filter;

        this.filterApplications();
    }

    filterApplications() {
        this.filteredApplications = this.applications;

        if (this.applicationsFilter.name) {
            this.filterApplicationsByCandidateProperty('name', 'name');
        }

        if (this.applicationsFilter.city) {
            this.filterApplicationsByCandidateProperty('city', 'city');
        }

        if (this.applicationsFilter.position) {
            this.filterApplicationsByCandidateProperty('position', 'position');
        }

        if (this.applicationsFilter.speciality) {
            this.filterApplicationsByCandidateProperty('speciality', 'speciality');
        }

        if (this.applicationsFilter.grade) {
            this.filterApplicationsByCandidateProperty('grade', 'grade');
        }

        if (this.applicationsFilter.experience) {
            this.filterApplicationsByCandidateProperty('experience', 'experience');
        }

        if (this.applicationsFilter.workSchedule) {
            this.filterApplicationsByCandidateProperty('work_schedule', 'workSchedule');
        }

        if (this.applicationsFilter.applicationStatus) {
            this.filterApplicationsByApplicationProperty('status', 'applicationStatus');
        }

        console.log(this.filteredApplications.map((application) => application.candidate));
    }

    filterApplicationsByCandidateProperty(
        propertyName: keyof Candidate,
        filterName: keyof IApplicationsFilter
    ) {
        this.filteredApplications = this.filteredApplications.filter((application) => {
            if (application.candidate[propertyName] === null) {
                return false;
            }

            return application.candidate[propertyName]
                .toString()
                .toLowerCase()
                .includes(this.applicationsFilter[filterName]!.toLowerCase());
        });

        console.log(this.filteredApplications.map((application) => application.candidate));
    }

    filterApplicationsByApplicationProperty(
        propertyName: keyof Application,
        filterName: keyof IApplicationsFilter
    ) {
        this.filteredApplications = this.filteredApplications.filter((application) => {
            return application[propertyName]
                .toString()
                .toLowerCase()
                .includes(this.applicationsFilter[filterName]!.toLowerCase());
        });
    }

    async fetchApplications() {
        this.isApplicationsLoading = true;

        return ApplicationsApiService.fetchApplications({})
            .then((applications) => {
                this.applications = applications;
                this.filteredApplications = applications;

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
