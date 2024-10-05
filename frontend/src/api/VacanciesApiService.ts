import axios from 'axios';

import { API_URL } from '@/config';
import { Candidate, FetchVacancyColdCandidatesParams } from './models';

class VacanciesApiService {
    public async fetchVacancyColdCandidates({ vacancyId }: FetchVacancyColdCandidatesParams) {
        const response = await axios.get<Candidate[]>(
            `${API_URL}/api/v1/vacancies/${vacancyId}/candidates`
        );

        return response.data;
    }
}

export default new VacanciesApiService();
