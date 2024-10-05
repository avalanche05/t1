import { observer } from 'mobx-react-lite';
import CandidateCard from '@/components/candidate/CandidateCard';
import { useEffect } from 'react';
import { useStores } from '@/hooks/useStores';
import { toast } from '@/components/ui/use-toast';
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs';
import { Skeleton } from '@/components/ui/skeleton';
import ApplicationsFilter from '@/components/ApplicationsFilter';

const Applications = observer(() => {
    const { rootStore } = useStores();

    useEffect(() => {
        rootStore.fetchApplications().catch(() => {
            toast({
                title: 'Ошибка',
                description: 'Не удалось загрузить отклики',
                variant: 'destructive',
            });
        });
    }, [rootStore]);

    return (
        <div className='container mx-auto p-4'>
            <ApplicationsFilter />

            <Tabs defaultValue='applications' className='w-full'>
                <TabsList className='grid w-full grid-cols-2'>
                    <TabsTrigger value='applications'>Отклики</TabsTrigger>
                    <TabsTrigger value='coldCandidates'>
                        Подходящие кандидаты без отклика
                    </TabsTrigger>
                </TabsList>
                <TabsContent value='applications'>
                    {rootStore.isApplicationsLoading ? (
                        <>
                            {Array.from({ length: 5 }).map((_, index) => (
                                <Skeleton key={index} className='bg-slate-200 h-40 w-full mt-5' />
                            ))}
                        </>
                    ) : (
                        rootStore.filteredApplications.map((application) => (
                            <CandidateCard
                                key={application.candidate.id}
                                candidate={application.candidate}
                                application={application}
                            />
                        ))
                    )}
                </TabsContent>
                <TabsContent value='coldCandidates'>
                    {rootStore.vacancyColdCandidates.map((candidate) => (
                        <CandidateCard key={candidate.id} candidate={candidate} />
                    ))}
                </TabsContent>
            </Tabs>
        </div>
    );
});

export default Applications;
