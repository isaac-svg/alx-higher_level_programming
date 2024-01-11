
  struct ListNode {
      int val;
      ListNode *next;
      ListNode() : val(0), next(nullptr) {}
      ListNode(int x) : val(x), next(nullptr) {}
      ListNode(int x, ListNode *next) : val(x), next(next) {}
  };
 
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        
        ListNode *current = list1;
        ListNode *temp = list2;
        ListNode *mergeHead = new ListNode();
        ListNode *tempMerge = mergeHead;

         while (current != nullptr && temp != nullptr) {
            if (current->val < temp->val) {
                tempMerge->next = current;
                current = current->next;
            } else {
                tempMerge->next = temp;
                temp = temp->next;
            }
            tempMerge = tempMerge->next;
        }

        // Append the remaining nodes from list1 or list2
        if (current != nullptr) {
            tempMerge->next = current;
        } else {
            tempMerge->next = temp;
        }

        // The head of the merged list is the next of the dummy node
        return mergeHead->next;
    }
};


int main()
{
    
}