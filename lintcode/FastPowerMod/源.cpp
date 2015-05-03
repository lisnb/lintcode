#include <iostream>
using namespace std;



class Solution {
public:
    /*
    * @param a, b, n: 32bit integers
    * @return: An integer
    */
    int fastPower(int a, int b, int n) {
        // write your code here
        if (b == 1)
            return 0;
        if (a == 1)
            return a%b;
        return PowerMod(a, n, b);
    }

    int PowerMod(int a, int b, int c)
    {
        long long ans = 1;
        long long tmp = a;
        tmp = tmp % c;
        while (b>0) {
            cout << ans << endl;
            if (b&0x1)
                ans = (ans * tmp) % c;
            b >>= 1;
            tmp = (tmp * tmp) % c;
        }
        return ans;
    }
};



int main()
{
    Solution s;
    cout << s.fastPower(2, 2147483647, 2147483647) << endl;
    system("pause");


}