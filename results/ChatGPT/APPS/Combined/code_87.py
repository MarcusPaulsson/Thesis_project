def max_projects(n, r, projects):
    # Sort projects by their required rating (a_i)
    projects.sort(key=lambda x: x[0])
    
    count = 0
    current_rating = r
    
    # Try to complete projects in sorted order
    for a_i, b_i in projects:
        if current_rating >= a_i:  # Check if we can start the project
            count += 1  # We can complete this project
            current_rating += b_i  # Update the rating after completing the project
            
            if current_rating < 0:  # Ensure rating does not drop below zero
                break
    
    return count

def main():
    # Read input
    n, r = map(int, input().split())
    projects = [tuple(map(int, input().split())) for _ in range(n)]

    # Get the maximum number of projects that can be completed
    result = max_projects(n, r, projects)

    # Print the result
    print(result)

if __name__ == "__main__":
    main()