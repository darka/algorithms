class Solution {
public:
    int findMin(vector<int> &num) {
        if (num.size() == 0)
            return 0;
        return findMin(num, 0, num.size());
    }

    int findMin(vector<int> &num, size_t a, size_t b) {
        if (num[a] <= num[b-1]) {
            return num[a];
        } else {
            size_t mid = a + (b - a) / 2;
            if (num[a] > num[mid-1])
                return findMin(num, a, mid);
            else
                return findMin(num, mid, b);
        }
    }
};
