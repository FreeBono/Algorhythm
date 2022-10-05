```csharp
using System;

public class Solution {
    public int[] solution(int[] array, int[,] commands) {
        int[] answer = new int[commands.GetLength(0)];

        for (int i = 0 ; i < commands.GetLength(0); i++) {
            int[] temp = new int[commands[i,1]-commands[i,0]+1];
            // Console.WriteLine(commands[i,1]-commands[i,0]+1);
            for (int j = 0 ; j < commands[i,1]-commands[i,0]+1 ;  j++) {
                temp[j] = array[j+commands[i,0]-1];
                
            }
            Array.Sort(temp);
            
            answer[i] = temp[commands[i,2]-1];
            // Console.WriteLine(temp[commands[i,2]]);
            
        }
        return answer;
    }
}
```

