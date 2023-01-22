class Solution
{

	  int select(int arr[], int i)
{
    	 int selected=arr[i];
    // code here such that selecionSort() sorts arr[]
      int size=arr.length;
      for (int j=i;j<size;j++){
            if (arr[j]<selected){
                selected=arr[j];
            } 
    }
     return selected;
};
   
void selectionSort(int arr[], int n)
{
  //code here
  for (int i=0;i<n;i++){
      for (int j=i;j<n;j++)
        if (arr[j]==this.select(arr,i)){
          int tmp=arr[i];
          arr[i]=this.select(arr,i);
          arr[j]=tmp;
      }
  }
};
}	 		
      
      
      
      
      
      
      
      
      
      class Solution
{

	  int select(int arr[], int i)
{
    	 int selected=arr[i];
    // code here such that selecionSort() sorts arr[]
      int size=arr.length;
      for (int j=i;j<size;j++){
            if (arr[j]<selected){
                selected=arr[j];
            } 
    }
     return selected;
};
   
void selectionSort(int arr[], int n)
{
  //code here
  for (int i=0;i<n;i++){
      for (int j=i;j<n;j++)
        if (arr[j]==this.select(arr,i)){
          int tmp=arr[i];
          arr[i]=this.select(arr,i);
          arr[j]=tmp;
      }
  }
};
}
