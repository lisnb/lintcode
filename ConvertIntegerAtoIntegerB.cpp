/* 
* @Author: lisnb
* @Date:   2015-05-02 10:56:04
* @Last Modified by:   lisnb
* @Last Modified time: 2015-05-02 11:14:25
*/

#include <iostream>

using namespace std;


class Solution {
public:
    /**
     *@param a, b: Two integer
     *return: An integer
     */
    int bitSwapRequired(int a, int b) {
        // write your code here
        int c(a^b), cnt(0);
        if (c<0)
        {
            c&=((1<<31)-1);
            cnt+=1;
        }
        while(c!=0)
        {
            cout<<c<<endl;
            cnt+=c&1;
            c>>=1;
        }
        return cnt;
    }
};


int main(){
    Solution s;
    cout<<s.bitSwapRequired(1, -1)<<endl;
    int a = -1&((1<<31)-1);
    cout<<a<<endl;
    return 0;
}