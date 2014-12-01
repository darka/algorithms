class MinStack {
public:
    void push(int x) {
        normalStack.push(x);
        // Try not to push duplicate elements onto minStack to save memory
        if (minStack.empty() || getMin() >= x) {
            minStack.push(x);
        }
    }

    void pop() {
        if (top() == getMin())
            minStack.pop();
        normalStack.pop();
    }

    int top() {
        return normalStack.top();
    }

    int getMin() {
        return minStack.top();
    }
private:
    stack<int> normalStack;
    stack<int> minStack;
};
