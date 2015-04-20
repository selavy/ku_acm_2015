#include <iostream>
#include <string>
#include <algorithm>

int main(int argc, char ** argv) {
    int n;
    std::cin >> n;
    for (int i = 0; i < n; ++i) {
        std::string perm, word;
        std::cin >> word;
        perm = word;
        std::sort(perm.begin(), perm.end());
        int count = 1;
        for (;perm != word && std::next_permutation(perm.begin(), perm.end()); ++count);
        std::cout << count << std::endl;
    }
    return 0;
}
