#include <iostream>
#include <vector>
#include <string>
#include <memory>
#include <queue>
#include <unordered_map>
using namespace std;

// declaration of MenuTree Node
class Node {
public:
    string key; // 唯一键值
    int value;  // 节点的整数值
    bool active; // 是否是激活状态
    vector<shared_ptr<Node>> children;
    Node(const string& key, int value, bool active) : key(key), value(value), active(active) {}
};

//
class MenuTree {
private:
    shared_ptr<Node> root;
    
    //print children node recursively
    void printTree(shared_ptr<Node> node, int depth) {
        if (!node) return;
        string activeStatus = node->active ? "active" : "inactive";
        cout << string(depth * 2, ' ') << node->key << " [" << node->value << "] " << activeStatus << endl;
        for(const auto& child : node->children) {
            printTree(child, depth + 1);
        }
    }

    // find node by key recursively
    shared_ptr<Node> findNode(shared_ptr<Node> node, const string& targetKey) {
        if(!node) return nullptr;
        if(node->key == targetKey) return node;
        for(const auto& child : node->children) {
            auto found = findNode(child, targetKey);
            if(found) return found;
        }
        return nullptr;
    }

public:
    MenuTree(){
        root = make_shared<Node>("root", 0);
    }

    // add node to the menu tree
    bool addMenu(const string& parentKey, const string& key, int childValue) {
        //first find the parent node
        auto parentNode = findNode(root, parentKey);
        if(!parentNode) {
            cout << "Parent node not found" << parentKey<< endl;
            return false;
        }
        parentNode->children.push_back(make_shared<Node>(key, childValue, true));
        return true;
    }

    bool deactivateMenu(const string& targetKey) {
        auto targetNode = findNode(root, targetKey);
        if(!targetNode) {
            cout << "Target node not found" << targetKey << endl;
            return false;
        }
        targetNode->active = false;
        return true;
    }

    //delete node from the menu tree
    bool deleteMenu(const string& targetKey) {
        if (root->key == targetKey) {
            cout << "Cannot delete root node" << endl;
            return false;
        }
        queue<shared_ptr<Node>> q;
        q.push(root);
        while(!q.empty()) {
            auto current = q.front();
            q.pop();
            for(auto it = current->children.begin(); it != current->children.end(); ++it) {
                if((*it)->key == targetKey) {
                    current->children.erase(it);
                    return true;
                }
                q.push(*it);
            }
        }
        cout << "Target node not found" << targetKey << endl;
        return false;
    }

    shared_pt<Node> findMenu(const string& targetKey) {
        return findNode(root, targetKey);
    }

    void printMenu() {
        printTree(root, 0);
    }
};

int main() {
    MenuTree menuTree;
    // add menu
    menuTree.addMenu("Root", "File", 1);
    menuTree.addMenu("Root", "Edit", 2);
    menuTree.addMenu("File", "New", 3);
    menuTree.addMenu("File", "Open", 4);
    menuTree.addMenu("Edit", "Copy", 5);
    menuTree.addMenu("Edit", "Paste", 6);
    menuTree.addMenu("Edit", "Delete", 7);

    // print menu
    cout << "Initial Menu Tree" << endl;
    menuTree.printMenu();

    // deactivate a item from menu
    menuTree.deactivateMenu("Copy");
    cout << "\nAfter deactivating 'Copy':" << endl;
    menuTree.printMenu();

    // delete a item from menu
    menuTree.deleteMenu("Open");
    cout << "\nAfter deleting 'Open':" << endl;
    menuTree.printMenu();

    return 0;
}
