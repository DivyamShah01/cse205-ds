class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:

        max=0
        for i in range(len(tickets)):
            if max<tickets[i]:
                max=tickets[i]
        #print(max)
        time=0

        for i in range(max):

            for j in range(len(tickets)):

                if tickets[k]==0:
                    return time

                if tickets[j]>0:
                    tickets[j]-=1
                    
                    time+=1
                
                elif tickets[j]==0:
                    #print(time)
                    #print(tickets[j])
                    if tickets[k]==0:
                        return time
                    else:
                        continue
                else:
                    continue
                #print(time)
        return time