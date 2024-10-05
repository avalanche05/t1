import axios from 'axios';

import { API_URL } from '@/config';
import {
    Candidate,
    CreateVacancyParams,
    FetchVacancyColdCandidatesParams,
    FetchVacancyParams,
} from './models';

class VacanciesApiService {
    public async fetchVacancyColdCandidates({ vacancyId }: FetchVacancyColdCandidatesParams) {
        const response = await axios.get<Candidate[]>(
            `${API_URL}/api/v1/vacancies/${vacancyId}/candidates`
        );

        return response.data;
    }

    public async createVacancy(params: CreateVacancyParams) {
        const response = await axios.post(`${API_URL}/api/v1/vacancies`, params);

        return response.data;
    }

    public async fetchVacancies(params: FetchVacancyParams) {
        const response = await axios.get(`${API_URL}/api/v1/vacancies`, { params });

        return response.data;
    }
}

export default new VacanciesApiService();
