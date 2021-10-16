#include <cstdlib>
// Integer class 

class Integer{
	public:
		Integer(int);
		int get();
		int fib();
		void set(int);
	private:
		int val;
		int fibb(int);
	};


Integer::Integer(int n){
	val = n;
	}


int Integer::fibb(int n){
	if (n <= 1){
		return n;
	} else {
		return (fibb(n - 1) + fibb(n - 2));
	}
}


int Integer::get(){
	return val;
	}


void Integer::set(int n){
	val = n;
	}


int Integer::fib(){
	return fibb(val);
	}


extern "C"{
	Integer* Integer_new(int n) {return new Integer(n);}
	int Integer_get(Integer* integer) {return integer->get();}
	void Integer_set(Integer* integer, int n) {integer->set(n);}
	int Intgeger_fib(Integer* integer) {return integer->fib();}
	void Integer_delete(Integer* integer){
		if (integer){
			delete integer;
			integer = nullptr;
			}
		}
	}
