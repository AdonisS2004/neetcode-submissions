class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        return (checkRow(board)
                && checkCol(board)
                && checkGrid(board));
    }
    bool checkRow(vector<vector<char>>& board){
        for(vector<char> row: board){
            unordered_set<char> seen;
            for(char col: row){
                if(col != '.' && seen.find(col) != seen.end()){
                    return false;
                }
                seen.insert(col);
            }
        }
        return true;
    }
    bool checkCol(vector<vector<char>>& board){
        int col = 0;
        while (col < 9){
            unordered_set<char> seen;
            for(int row = 0; row < 9; row++){
                if (board[row][col] != '.' && 
                    seen.find(board[row][col]) != seen.end()){
                        return false;
                }
                seen.insert(board[row][col]);
            }
            col++;
        }
        return true;
    }
    bool checkGrid(vector<vector<char>>& board){
        vector<int> rows = {1, 4, 7};
        vector<int> cols = {1, 4, 7};
        vector<int> offsets = {-1, 0, 1};

        for(int row: rows){
            for(int col: cols){
                vector<tuple<int, int>> coords = {
                    {row - 1,col - 1},
                    {row - 1,col},
                    {row - 1,col + 1},
                    {row,col - 1},
                    {row,col},
                    {row,col + 1},
                    {row + 1,col - 1},
                    {row + 1,col},
                    {row + 1,col + 1},
                };
                unordered_set<char> seen;
                for (auto const& [row, col]: coords){
                    if (board[row][col] != '.'
                    && seen.find(board[row][col]) != seen.end()){
                        return false;
                    }
                    seen.insert(board[row][col]);
                }
            }
        }
        return true;
    }
};
