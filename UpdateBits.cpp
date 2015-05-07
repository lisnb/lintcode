/* 
* @Author: lisnb
* @Date:   2015-05-04 23:54:36
* @Last Modified by:   lisnb
* @Last Modified time: 2015-05-05 00:15:53
*/

#include <iostream>
#include <bitset>

using namespace std;


class Solution {
public:
    /**
     *@param n, m: Two integer
     *@param i, j: Two bit positions
     *return: An integer
     */
    int updateBits(int n, int m, int i, int j) {
        // write your code here
        int mask1(0xffffffff);
        if(j==31)
        	mask1 = 0;
        else
        	mask1<<=(j+1);
        bitset<32> b1(mask1);
        cout<<b1<<endl;
        int mask2(0);
        if(i!=0)
        {
        	mask2 = 0x1;
        	for(auto k=0;k<i-1;++k)
        	{
        		mask2<<=1;
        		mask2|=1;
        		//cout<<mask2<<endl;
        	}
        }
        //mask2>>=(32-i);
        bitset<32> b2(mask2);
        cout<<b2<<endl;
        int mask3 = mask1|mask2;
        bitset<32> b3(mask3);
        cout<<b3<<endl;
        int nn = n&mask3;
        bitset<32> b4(nn);
        cout<<b4<<endl;
        int mm = m<<i;
        bitset<32> b5(mm);
        cout<<b5<<endl;
        int r = nn|mm;
        bitset<32> b6(r);
        cout<<b6<<endl;
        return r;
    }
};



int main(){
	Solution s;
	cout<<s.updateBits(-521,0,31,31)<<endl;
    return 0;
}