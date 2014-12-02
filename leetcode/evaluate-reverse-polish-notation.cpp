class Solution {
public:
    int execute(char op, int a, int b) {
        switch(op) {
            case '+': return a + b;
            case '-': return a - b;
            case '/': return a / b;
            case '*': return a * b;
        }
    }
    
    int evalRPN(vector<string> &tokens) {
        if (tokens.empty())
            return 0;
            
        stack<int> s;
        for (vector<string>::iterator i = tokens.begin(); i != tokens.end(); ++i) {
            if (*i == "+" || *i == "-" || *i == "/" || *i == "*") {
                int b = s.top();
                s.pop();
                int a = s.top();
                s.pop();
                
                s.push(execute((*i)[0], a, b));
                
            } else {
                stringstream ss;
                ss << (*i);
                
                int n = 0;
                ss >> n;
                s.push(n);
            }
            
        }
        return s.top();
    }
};
