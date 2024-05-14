class Node {
	constructor(value) {
		this.value = value;
		this.next = null;
	}
}

class Queue {
	constructor(value) {
		const newNode = new Node(value);
		this.first = newNode; // First node to be out
		this.last = newNode; // Last node to be out
		this.length = 1;
	}

	enqueue(value) {
		const newNode = new Node(value);

		if (this.length === 0) {
			this.first = newNode;
			this.last = newNode;
		} else {
			this.last.next = newNode;
			this.last = newNode;
		}

		this.length++;
		return this;
	}

	dequeue() {
		let temp = this.first;

		if (this.length === 0) return undefined;
		else if (this.length === 1) {
			this.first = null;
			this.last = null;
		} else {
			this.first = this.first.next;
			temp.next = null;
		}

		this.length--;
		return this;
	}

	toArray() {
		const arr = [];

		let node = this.first;

		for (let i = 0; i < this.length; i++) {
			arr.push(node.value);
			node = node.next;
		}

		return arr;
	}
}

const queue = new Queue(10);
console.log(queue.toArray());

queue.enqueue(20);
console.log(queue.toArray());

queue.enqueue(30);
console.log(queue.toArray());

queue.dequeue();
console.log(queue.toArray());

queue.dequeue();
console.log(queue.toArray());

queue.enqueue(200);
console.log(queue.toArray());
