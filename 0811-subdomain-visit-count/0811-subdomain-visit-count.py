class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        visited={}
        for domain in cpdomains:
           
            dom_info=domain.split(" ")
            visit=int(dom_info[0])
            dom_names=dom_info[1].split(".")
            size=len(dom_names)-1
            size_len=len(dom_names)-1
            while size>=0:

                sub_domian=""
                num2=size_len-size
                while size_len>=num2:

                    if num2==size_len:

                        sub_domian+=dom_names[num2]

                    else:

                        sub_domian+=dom_names[num2]+"."

                    num2+=1

                size-=1

                if sub_domian in visited:

                    visited[sub_domian]+=visit

                else:

                    visited[sub_domian]=visit

        cp_domains=[]
        for key,value in visited.items():
            cp_domains.append(str(value)+" "+key)
        return cp_domains
