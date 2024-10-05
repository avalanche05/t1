import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card';
import { Candidate } from '@/api/models/cadidates';
import { Application, ApplicationStatuses } from '@/api/models';
import CandidateCard from '@/components/candidate/CandidateCard';

// Mock data with extended candidate information
const mockApplications: Application[] = [
    {
        id: 1,
        candidate: {
            id: 1,
            name: 'John Doe',
            phone: '+1 (555) 123-4567',
            email: 'john.doe@example.com',
            contacts: 'LinkedIn: johndoe',
            skills: ['JavaScript', 'React', 'Node.js'],
            experience: 5,
            position: 'Frontend Developer',
            grade: 'Senior',
            speciality: 'Frontend Developer',
            education: 'BS in Computer Science',
            resumeLink: 'https://example.com/johndoe_resume.pdf',
            summary: 'summary',
            isCold: false,
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
        status: ApplicationStatuses.CandidateAccepted,
        createdAt: 'string',
    },
];

const mockOtherCandidates: Candidate[] = [
    {
        id: 2,
        name: 'John Doe',
        phone: '+1 (555) 123-4567',
        email: 'john.doe@example.com',
        contacts: 'LinkedIn: johndoe',
        skills: ['JavaScript', 'React', 'Node.js'],
        experience: 5,
        position: 'Frontend Developer',
        grade: 'Senior',
        speciality: 'Frontend Developer',
        education: 'BS in Computer Science',
        resumeLink: 'https://example.com/johndoe_resume.pdf',
        summary: 'summary',
        isCold: false,
    },
];

export default function Applications() {
    return (
        <div className='container mx-auto p-4'>
            <h1 className='text-2xl font-bold mb-4'>HR Monitor</h1>

            <div className='grid grid-cols-1 md:grid-cols-2 gap-4'>
                <Card>
                    <CardHeader>
                        <CardTitle>Отклики</CardTitle>
                    </CardHeader>
                    <CardContent>
                        {mockApplications.map((application) => (
                            <CandidateCard
                                key={application.candidate.id}
                                candidate={application.candidate}
                            />
                        ))}
                    </CardContent>
                </Card>

                <Card>
                    <CardHeader>
                        <CardTitle>Другие кандидаты</CardTitle>
                    </CardHeader>
                    <CardContent>
                        {mockOtherCandidates.map((candidate) => (
                            <CandidateCard key={candidate.id} candidate={candidate} />
                        ))}
                    </CardContent>
                </Card>
            </div>
        </div>
    );
}
