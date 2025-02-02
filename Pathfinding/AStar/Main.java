import java.util.*;

public class Main {
    public static void main(String[] args) {
        // Grid generation parameters
        int rows = 25;
        int cols = 25;

        // Create initial and final nodes
        Node initialNode = new Node(0, 0);
        Node finalNode = new Node(rows - 1, cols - 1);

        // Run the A* algorithm
        AStar aStar = new AStar(rows, cols, initialNode, finalNode);

        // Randomly generate block positions
        int numBlocks = 200; // Number of blocks to generate
        int[][] blocksArray = generateRandomBlocksArray(rows, cols, numBlocks);
        aStar.setBlocks(blocksArray);

        List<Node> path = aStar.findPath();

        // Print the path
        if (path.isEmpty()) {
            System.out.println("No path found.");
        } else {
            System.out.println("Path:");
            printPath(path);
            System.out.println();
        }
        System.out.println("Grid:");
        printGraph(path, blocksArray, rows, cols);
    }

    public static void printPath(List<Node> path) {
        for (Node node : path) {
            System.out.println(node);
        }
    }

    public static void printGraph(List<Node> path, int[][] blocksArray, int rows, int cols) {
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                boolean block = false;
                for (int[] b : blocksArray) {
                    if (i == b[0] && j == b[1]) {
                        block = true;
                        break;
                    }
                }
                boolean p = false;
                for (Node node : path) {
                    if (i == node.getRow() && j == node.getCol()) {
                        p = true;
                        break;
                    }
                }

                if (block) {
                    System.out.print("X ");
                } else if (p) {
                    System.out.print("■ ");
                } else {
                    System.out.print(". ");
                }
            }
            System.out.println();
        }
    }

    public static int[][] generateRandomBlocksArray(int rows, int cols, int numBlocks) {
        Random random = new Random();
        Set<List<Integer>> blockSet = new HashSet<>();

        while (blockSet.size() < numBlocks) {
            int row = random.nextInt(rows);
            int col = random.nextInt(cols);
            blockSet.add(Arrays.asList(row, col));
        }

        int[][] blocksArray = new int[numBlocks][2];
        int index = 0;
        for (List<Integer> block : blockSet) {
            blocksArray[index][0] = block.get(0);
            blocksArray[index][1] = block.get(1);
            index++;
        }

        return blocksArray;
    }
}
