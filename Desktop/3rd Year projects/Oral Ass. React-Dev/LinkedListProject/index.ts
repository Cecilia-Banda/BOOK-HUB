import { LinkedList } from './LinkedList';

const list = new LinkedList<number>();

list.add(10);
list.add(20);
list.add(30);

list.display();  // Output: 10, 20, 30

const found = list.find(20);
console.log(found?.data);  // Output: 20

list.remove(20);
list.display();  // Output: 10, 30
