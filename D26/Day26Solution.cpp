int visited[100005];
int counted[100005];
int isstack[100005];


class Solution{
    public:
    bool checkCycle(int i, vector<vector<int>> &ve) {
        if (isstack[i] == 1) return true;
    
        isstack[i] = 1;
        for (auto it : ve[i]) {
            if (visited[it] == 1) {
                if (isstack[it] == 1) return true;
                continue;
            }
            visited[it] = 1;
            if (checkCycle(it, ve)) return true;
        }
        isstack[i] = 0;
        return false;
    }
    int dfs(int i, vector<vector<int>> &ve, int duration[]) {
        if (counted[i] != -1) return counted[i];
        int x = 0;
    
        for (auto it : ve[i]) x = max(x, dfs(it, ve, duration));
        counted[i] = x + duration[i];
        return counted[i];
    }
    
    int minTime(vector<pair<int, int>> &vp, int duration[], int n, int m) {
        int independent[n + 5] = {0};
        vector<vector<int>> ve(n + 2);
        for (int i = 0; i < m; i++) {
            int x = vp[i].first;
            int y = vp[i].second;
            ve[x].push_back(y);
            independent[y]++;
        }
        memset(visited, -1, sizeof(visited));
        memset(counted, -1, sizeof(counted));
        memset(isstack, -1, sizeof(isstack));
    
        int flag = 0;
        for (int i = 0; i < n; i++)
            if (independent[i] == 0) flag = 1;
    
        if (flag == 0) return -1;
    
        for (int i = 0; i < n; i++) {
            if (independent[i] != 0) {
                continue;
            }
            visited[i] = 1;
            if (checkCycle(i, ve)) return -1;
        }
    
        int ans = 0;
        for (int i = 0; i < n; i++)
            if (independent[i] == 0) ans = max(ans, dfs(i, ve, duration));
    
        return ans;
    }
};
