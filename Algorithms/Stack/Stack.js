class Node {
	constructor(value) {
		this.value = value;
		this.next = null;
	}
}

class Stack {
	constructor(value) {
		this.top = new Node(value);
		this.length = 1;
	}

	push(value) {
		const newNode = new Node(value);

		if (this.length === 0) {
			this.top = newNode;
		} else {
			newNode.next = this.top;
			this.top = newNode;
		}

		this.length++;
		return this;
	}

	pop() {
		if (this.length === 0) return undefined;

		this.top = this.top.next;
		this.length--;

		return this;
	}

	toArray() {
		const arr = [];

		let node = this.top;

		for (let i = 0; i < this.length; i++) {
			arr.push(node.value);
			node = node.next;
		}

		return arr;
	}
}

const s = new Stack(10);
console.log(s.toArray());

s.push(20);
console.log(s.toArray());

s.push(30);
console.log(s.toArray());

s.pop();
console.log(s.toArray());

s.pop();
console.log(s.toArray());

s.push(200);
console.log(s.toArray());
