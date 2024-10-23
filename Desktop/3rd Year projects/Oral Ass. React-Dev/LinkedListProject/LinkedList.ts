// Node class definition
class Node<T> {
    data: T;
    next: Node<T> | null = null;

    constructor(data: T) {
        this.data = data;
    }
}

// LinkedList class definition
class LinkedList<T> {
    head: Node<T> | null = null;

    add(data: T): void {
        const newNode = new Node(data);
        if (!this.head) {
            this.head = newNode;
        } else {
            let current = this.head;
            while (current.next) {
                current = current.next;
            }
            current.next = newNode;
        }
    }

    remove(data: T): void {
        if (!this.head) return;

        if (this.head.data === data) {
            this.head = this.head.next;
            return;
        }

        let current = this.head;
        while (current.next && current.next.data !== data) {
            current = current.next;
        }

        if (current.next) {
            current.next = current.next.next;
        }
    }

    find(data: T): Node<T> | null {
        let current = this.head;
        while (current && current.data !== data) {
            current = current.next;
        }
        return current;
    }

    display(): void {
        let current = this.head;
        while (current) {
            console.log(current.data);
            current = current.next;
        }
    }
}

export { LinkedList };
