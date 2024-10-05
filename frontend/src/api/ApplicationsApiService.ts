import axios from 'axios';

import { API_URL } from '@/config';
import { Application, ApplicationStatus, FetchApplicationsParams } from './models';
import { Grade, WorkSchedule } from '@/models/IApplicationsFilter';

class ApplicationsApiService {
    public async fetchApplications(params: FetchApplicationsParams) {
        return new Promise<Application[]>((resolve) => {
            setTimeout(() => {
                resolve([
                    {
                        id: 1,
                        candidate: {
                            id: 1,
                            name: 'John Doe 123',
                            city: 'New York',
                            phone: '+1 (555) 123-4567',
                            email: 'john.doe@example.com',
                            contacts: 'LinkedIn: johndoe',
                            skills: ['JavaScript', 'React', 'Node.js'],
                            experience: 5,
                            position: 'Frontend Developer',
                            grade: Grade.Middle,
                            speciality: 'Frontend Developer',
                            education: 'BS in Computer Science',
                            resume_link: 'https://example.com/johndoe_resume.pdf',
                            summary: 'summary',
                            work_schedule: WorkSchedule.FullDay,
                            is_cold: false,
                        },
                        vacancy: {
                            id: 1,
                            position: 'string',
                            grade: 'string',
                            speciality: 'string',
                            description: 'string',
                            team: 'string',
                            createdAt: 'string',
                        },
                        status: ApplicationStatus.CandidateAccepted,
                        createdAt: 'string',
                    },
                ]);
            }, 500);
        });

        const response = await axios.get<Application[]>(`${API_URL}/api/v1/applications`, {
            params,
        });

        return response.data;
    }
}

export default new ApplicationsApiService();
