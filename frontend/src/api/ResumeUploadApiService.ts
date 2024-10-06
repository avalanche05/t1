import { get, post } from './http';
import { ResumeUploadResponse } from './models';

class ResumeUploadApiService {
    public async uploadFiles(
        files: File[],
        vacancy_id: number | undefined
    ): Promise<ResumeUploadResponse> {
        const formData = new FormData();

        files.forEach((file) => {
            formData.append('files', file);
        });

        const response = await post<ResumeUploadResponse>(`/api/v1/resumes`, formData, {
            headers: {
                'Content-Type': 'multipart/form-data',
            },
            timeout: 510000,
            params: {
                vacancy_id,
            },
        });

        return response;
    }

    public async fetchUploadStatus(sessionId: string): Promise<ResumeUploadResponse> {
        const response = await get<ResumeUploadResponse>(`/api/v1/resumes/${sessionId}`);

        return response;
    }
}

export default new ResumeUploadApiService();
