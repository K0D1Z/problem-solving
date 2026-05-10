#include <random>
#include <cmath>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> sortArray(vector<int> &nums) {
        if (nums.empty()) return nums;
        quickSort(nums, 0, nums.size() - 1);
        return nums;
    }

    void quickSort(vector<int> &nums, const int low, const int high) {
        if (low < high) {
            if (abs(low - high) > 10) {
                int const pivIdx = partitionRandom(nums, low, high);
                quickSort(nums, low, pivIdx - 1);
                quickSort(nums, pivIdx + 1, high);
            } else {
                int const pivIdx = lomutoPartition(nums, low, high);
                quickSort(nums, low, pivIdx - 1);
                quickSort(nums, pivIdx + 1, high);
            }
        }
    }

    int partitionRandom(vector<int> &nums, const int low, const int high) {
        std::random_device rd;
        std::mt19937 gen(rd());
        std::uniform_int_distribution<> distr(low, high);
        const int r = distr(gen);
        swap(nums[high], nums[r]);
        return lomutoPartition(nums, low, high);
    }


    static int lomutoPartition(vector<int> &nums, const int low, const int high) {
        const int pivot = nums[high];
        int i = low - 1;

        for (int j = low; j <= high - 1; j++) {
            if (nums[j] < pivot) {
                i++;
                swap(nums[i], nums[j]);
            }
        }
        swap(nums[i + 1], nums[high]);
        return i + 1;
    }
};