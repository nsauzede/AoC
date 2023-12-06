TARGET=puzzle

all: $(TARGET)

test: $(TARGET)
	./$(TARGET)

puzzle: test.o lib.o
	$(CC) -o $@ $^

clean:
	$(RM) $(TARGET) *.o
