class Solution {
public:
    bool isPalindrome(string s) {
        cout << "start, size: " << s.size() << endl;
        int len = s.size();
        int left = 0;
        int right = len-1;
        // Uppercase letters: [65, 90]
        // Lowercase letters: [97, 122]
        // Numbers: [48, 57]
        while (left<=right){
            while(left < len && (!(isupper(s[left])) 
                                    && !(islower(s[left])) 
                                    && !(isdigit(s[left])))){
                left++;
            }
            while(right > 0 && (!(isupper(s[right])) 
                                    && !(islower(s[right])) 
                                    && !(isdigit(s[right])))){
                right--;
            }
            cout << "left: " << left << s[left] << "; right: " << right << s[right] << endl;
            if(left<=right){
                char cleft = s[left];
                char cright = s[right];
                if(isupper(cleft)){
                    cleft = tolower(cleft);
                }
                if(isupper(cright)){
                    cright = tolower(cright);
                }
                if(cleft != cright){
                    return false;
                }
            }
            left++;
            right--;
        }
        return true;
    }
};
