#include <stdio.h>
#include <stdbool.h>

#define MAXQUEUE 7

struct queue {
    int items[MAXQUEUE];
    int front;
    int rear;
};

void insert(struct queue *queue, int value);
int dequeue(struct queue *queue);
bool isEmpty(struct queue *queue);
bool isFull(struct queue *queue);
void printQueue(struct queue *queue);

int main (int argc, char *argv[]) {
    
    struct queue *queue;
    queue->front = 0;
    queue->rear = -1;

    int items[MAXQUEUE] = {1, 2, 3, 5, 8, 13, 21};
    int i;

    for (i = 0; i < MAXQUEUE; i++) {
        insert(queue, items[i]);
    }

    printQueue(queue);

    insert(queue, 34);
    insert(queue, 55);

    printQueue(queue);

    printf("remove item from queue!\n");

    dequeue(queue);
    dequeue(queue);
    dequeue(queue);

    printQueue(queue);

    return 0;
}

void printQueue(struct queue *queue) {
    
    int i;

    for (i = 0; i < MAXQUEUE; i++) {
        printf("%d -> %d\n", i, queue->items[i]);
    }
}

bool isEmpty(struct queue *queue) {
    return queue->rear < queue->front;
}

bool isFull(struct queue *queue) {
    return queue->rear == MAXQUEUE-1 ? true : false;
}

void insert(struct queue *queue, int value) {
 
    if (isFull(queue)) {
        printf("queue overflow!\n");
    } else {
        queue->items[++queue->rear] = value;
    }
}

int dequeue(struct queue *queue) {

    if (isEmpty(queue)) {
        printf("queue empty!\n");
        return -1;
    } else {

        int value = queue->items[queue->front--];

        return value;
    }
}
