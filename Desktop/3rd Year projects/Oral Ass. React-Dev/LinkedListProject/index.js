"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
var LinkedList_1 = require("./LinkedList");
var list = new LinkedList_1.LinkedList();
list.add(10);
list.add(20);
list.add(30);
list.display(); // Output: 10, 20, 30
var found = list.find(20);
console.log(found === null || found === void 0 ? void 0 : found.data); // Output: 20
list.remove(20);
list.display(); // Output: 10, 30
