// Run: node HashTable.js
// Run dev mode: node --watch HashTable.js

class HashTable {
	constructor(size = 7) {
		this.dataMap = new Array(size);
	}

	// Big O: O(1)
	_hash(key) {
		let hash = 0;
		for (let i = 0; i < key.length; i++) {
			hash = (hash + key.charCodeAt(i) * i) % this.dataMap.length;
		}
		return hash;
	}

	// Big O: O(1)
	set(key, value) {
		const index = this._hash(key);
		if (!this.dataMap[index]) this.dataMap[index] = [];
		this.dataMap[index].push([key, value]);

		return this;
	}

	// Big O: O(1)
	get(key) {
		const index = this._hash(key);

		if (this.dataMap[index]) {
			for (let i = 0; i < this.dataMap[index].length; i++) {
				if (this.dataMap[index][i][0] === key) return this.dataMap[index][i][1];
			}
		}

		return undefined;
	}

	keys() {
		const keys = [];
		for (let i = 0; i < this.dataMap.length; i++) {
			const data = this.dataMap[i];
			if (data) {
				for (let j = 0; j < data.length; j++) {
					keys.push(data[j][0]);
				}
			}
		}
		return keys;
	}

	toArray() {
		const arr = [];

		for (let i = 0; i < this.dataMap.length; i++) {
			const data = this.dataMap[i];
			if (data) {
				if (data.length === 1) arr.push([data[0][0], data[0][1]]);
				else arr.push(data);
			}
		}

		return arr;
	}

	toObject() {
		const obj = {};
		for (let i = 0; i < this.dataMap.length; i++) {
			const data = this.dataMap[i];
			if (data) {
				const key = this._hash(data[0][0]);

				obj[key] = {};

				for (let j = 0; j < data.length; j++) {
					obj[key][data[j][0]] = data[j][1];
				}
			}
		}
		return obj;
	}

	toNestedObject() {
		const obj = {};
		for (let i = 0; i < this.dataMap.length; i++) {
			const data = this.dataMap[i];
			if (data) {
				const key = this._hash(data[0][0]);

				if (data.length === 1) {
					obj[key] = {
						key: data[0][0],
						value: data[0][1]
					}
				} else {
					obj[key] = {};

					for (let j = 0; j < data.length; j++) {
						obj[key][data[j][0]] = data[j][1];
					}
				}
			}
		}
		return obj;
	}
}

const hashTable = new HashTable();
hashTable.set("beep", 50).set("boop", 1400).set("foo", 70);
// hashTable.set("beep", 50);
// hashTable.set("boop", 1400).set("foo", 70);

console.log(hashTable.get("boop"), hashTable.get("beep"), hashTable.get("false"));
console.log(hashTable.keys());
console.log(hashTable.toObject());
