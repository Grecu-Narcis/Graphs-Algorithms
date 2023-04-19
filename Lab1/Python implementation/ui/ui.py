from domain.directed_graph import *

class UI:
    def __init__(self):
        pass

    @staticmethod
    def print_menu():
        print("\nEnter 1 to get the number of vertices.")
        print("Enter 2 to print the set of vertices.")
        print("Enter 3 to check if an edge exists.")
        print("Enter 4 to get the in degree and out degree for a vertex.")
        print("Enter 5 to print the set of inbound edges of a specified vertex.")
        print("Enter 6 to print the set of outbound edges of a specified vertex.")
        print("Enter 7 to add a vertex.")
        print("Enter 8 to remove a vertex.")
        print("Enter 9 to add an edge.")
        print("Enter 10 to remove an edge.")
        print("Enter 11 to read a graph from a file - function 1.")
        print("Enter 12 to read a graph from a file - function 2.")
        print("Enter 13 to save the graph to a file.")
        print("Enter 14 to create a random graph.")
        print("Enter 15 to exit.")

    def main_menu(self):
        graph = read_graph_from_file_1("graph.txt")

        while True:
            UI.print_menu()

            option = input("Your option is: ")

            if option == "1":
                print("The number of vertices in graph is:", graph.get_number_of_vertices())

            elif option == "2":
                vertices = graph.get_set_of_vertices()
                if graph.get_number_of_vertices() == 0:
                    print("The graph does not contain any node.")
                    continue

                print("Vertices in the graph are:", end=" ")
                for vertex in vertices:
                    print(vertex, end=" ")
                print()

            elif option == "3":
                first_node = int(input("Enter the edge:\nFirst node: "))
                second_node = int(input("Second node: "))

                if graph.is_edge((first_node, second_node)):
                    print(f"Edge ({first_node}, {second_node}) exists.")
                else:
                    print(f"Edge ({first_node}, {second_node}) does not exist.")

            elif option == "4":
                vertex = input("Enter the vertex: ")
                try:
                    vertex_int = int(vertex)
                    try:
                        print("In degree:", graph.get_in_degree(vertex_int))
                        print("Out degree:", graph.get_out_degree(vertex_int))
                    except ValueError as ve:
                        print(ve)
                except ValueError as e:
                    print("Vertex must be an integer.")
                    continue

            elif option == "5":
                vertex = input("Enter the vertex: ")
                try:
                    vertex_int = int(vertex)
                    try:
                        edges = graph.get_in_bound_edges(vertex_int)
                        if len(edges) == 0:
                            print("There are no in bound edges.")
                            continue
                        str_edges = []
                        for edge in edges:
                            str_edges.append("{" + str(edge[0]) + ", " + str(edge[1]) + "}")
                        print("Edges are:", end=" ")
                        for edge in str_edges:
                            print(edge, end=" ")
                    except ValueError as ve:
                        print(ve)
                except ValueError as e:
                    print(e)


            elif option == "6":

                vertex = input("Enter the vertex: ")

                try:
                    vertex_int = int(vertex)
                except ValueError as ve:
                    print("Vertex must be an integer.")
                    continue

                try:
                    edges = graph.get_out_bound_edges(vertex_int)

                    if len(edges) == 0:
                        print("There are no in bound edges.")

                        continue

                    str_edges = []

                    for edge in edges:
                        str_edges.append("{" + str(edge[0]) + ", " + str(edge[1]) + "}")

                    print("Edges are: ", end="")

                    for edge in str_edges:
                        print(edge, end=" ")

                    print()

                except Exception as ve:

                    print(ve)

                    continue


            elif option == "7":
                vertex = input("Enter vertex: ")

                try:
                    vertex_int = int(vertex)
                    graph.add_vertex(vertex_int)
                    print("Vertex added successfully!")

                except ValueError:
                    print("Vertex should be an integer.")
                    continue

                except Exception as e:
                    print(e)
                    continue

            elif option == "8":
                vertex = input("Enter vertex: ")

                try:
                    vertex_int = int(vertex)
                    graph.remove_vertex(vertex_int)
                    print("Vertex removed successfully!")

                except ValueError:
                    print("Vertex should be an integer.")
                    continue

                except Exception as e:
                    print(e)
                    continue

            elif option == "9":
                print("Enter the edge you want to add")
                first_node = input("First node: ")
                second_node = input("Second node: ")
                cost = input("Cost: ")

                try:
                    first_node_int = int(first_node)
                    second_node_int = int(second_node)
                    cost_int = int(cost)
                    graph.add_edge((first_node_int, second_node_int), cost)
                    print("Edge added successfully!")

                except ValueError:
                    print("Vertex should be an integer.")
                    continue

                except Exception as e:
                    print(e)
                    continue

            elif option == "10":
                print("Enter the edge you want to remove: ")
                first_node = input("First node: ")
                second_node = input("Second node: ")

                try:
                    first_node_int = int(first_node)
                    second_node_int = int(second_node)
                    graph.remove_edge((first_node_int, second_node_int))
                    print("Edge removed successfully!")

                except ValueError:
                    print("Vertex should be an integer.")
                    continue

                except Exception as e:
                    print(e)
                    continue

            elif option == "11":
                file_name = input("Enter file name: ")
                graph = read_graph_from_file_1(file_name)
                print("Graph read from file successfully!")

            elif option == "12":
                file_name = input("Enter file name: ")
                graph = read_graph_from_file_2(file_name)
                print("Graph read from file successfully!")

            elif option == "13":
                file_name = input("Enter file name: ")
                write_graph_to_file(file_name, graph)
                print("Graph written to file successfully!")

            elif option == "14":
                number_of_vertices = int(input("Enter number of vertices: "))
                number_of_edges = int(input("Enter number of edges: "))
                graph = generate_random_graph(number_of_vertices, number_of_edges)
                print("Graph created successfully!")

            elif option == "15":
                break