/*
Day 19: Interfaces

The AdvancedArithmetic interface and the method declaration
for the abstract int divisorSum(int n) method are provided
for you in the editor below. Write the Calculator class, which
implements the AdvancedArithmetic interface. The implementation
for the divisorSum method must be public and take an integer parameter
'n' and return the sum of all its divisors. 
*/

#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
class AdvancedArithmetic{
    public:
        virtual int divisorSum(int n)=0;
};

class Calculator : public AdvancedArithmetic{
    public:
        virtual int divisorSum(int n) {
            int sum = 0;
            for(int i = 1; i <= n; i++) {
                if(n % i == 0) { sum += i; }
            }
            return sum;
        }
};

int main(){
    int n;
    cin >> n;
    AdvancedArithmetic *myCalculator = new Calculator();
    int sum = myCalculator->divisorSum(n);
    cout << "I implemented: AdvancedArithmetic\n" << sum;
    return 0;
}
