# **Interactive Graph Visualization Tool - Architecture Breakdown**

## **1. Overview**
This tool allows users to:
- **Create and edit graphs interactively.**
- **Generate predefined graph structures** (paths, cycles, caterpillars, Peterson graphs, random graphs, etc.).
- **Run built-in and user-submitted graph algorithms** with step-by-step animations.
- **Store and load user-generated graphs.**
- **Host the tool online** for public use.

---

## **2. Tech Stack**

| Layer        | Technology        | Purpose |
|-------------|------------------|---------|
| **Frontend** | React + Vis.js / D3.js | Interactive graph drawing and visualization |
| **Backend** | FastAPI + NetworkX | Graph generation, storage, and algorithm processing |
| **Database** | Supabase (PostgreSQL) | Stores user-generated graphs and metadata |
| **Code Execution** | Docker (Sandbox) / Pyodide | Securely runs user-submitted Python algorithms |
| **Hosting** | Vercel (Frontend), Render/Fly.io (Backend), Supabase (DB) | Online availability |

---

## **3. Frontend (React + Vis.js/D3.js)**
### **Graph Editor UI**
- Users can **click to add vertices**, **drag to create edges**, and **modify graph properties**.
- Uses **Vis.js** (simpler) or **D3.js** (more flexible) for rendering.
- Users can **switch between predefined graph types** (e.g., paths, cycles, caterpillars).

### **Algorithm Runner**
- Users can run **built-in and custom algorithms**.
- Step-by-step visualization (highlights visited nodes/edges dynamically).

### **User-Submitted Code Editor**
- Integrated **Python editor** (e.g., Monaco Editor from VS Code).
- Allows users to **highlight nodes/edges** as input.
- Runs code in a **secure backend environment**.

### **Graph Storage & Loading**
- Users can **export graphs as JSON or GraphML**.
- Users can **load previously saved graphs from Supabase**.

---

## **4. Backend (FastAPI + NetworkX + Execution Sandbox)**
### **Graph Generation API**
```http
GET /generate/path/{length}    # Returns a path graph
GET /generate/cycle/{length}   # Returns a cycle graph
GET /generate/peterson         # Returns a Peterson graph
GET /generate/random?nodes=N&edges=E  # Returns a random graph
```

### **Graph Algorithms API**
```http
POST /run/bfs            # Runs BFS and returns step-by-step state
POST /run/dijkstra       # Runs Dijkstra’s algorithm
POST /run/coloring       # Returns a valid graph coloring
```

### **Graph Storage API**
```http
POST /save               # Saves a user-generated graph to Supabase
GET /load/{graph_id}     # Loads a previously saved graph
```

### **User Algorithm Execution API**
```http
POST /execute            # Runs user-submitted Python code on a graph
```
- **Validates and executes** user-submitted code securely.
- **Restricts access** to OS functions, network calls, and dangerous operations.

---

## **5. Database (Supabase/PostgreSQL)**
### **Schema**
```sql
CREATE TABLE graphs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    name TEXT NOT NULL,
    graph_data JSONB NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
);
```
- Stores **graph structure as JSON**.
- Allows **user authentication (optional for private graphs).**

---

## **6. User-Submitted Algorithm Execution**
### **User API for Graph Processing**
Users write Python code using a predefined API:
```python
# Example user-defined function
def my_algorithm(graph):
    nodes = graph.get_nodes()
    edges = graph.get_edges()
    highlighted = graph.get_highlighted()
    results = {}
    for node in highlighted:
        results[node] = graph.get_neighbors(node)
    return results
```
#### **Graph Query Methods**
| Method | Purpose |
|--------|---------|
| `graph.get_nodes()` | Returns all nodes in the graph. |
| `graph.get_edges()` | Returns all edges (with weights if applicable). |
| `graph.get_neighbors(node)` | Returns adjacent nodes. |
| `graph.get_highlighted()` | Returns the nodes/edges currently selected. |

### **Execution Sandbox**
- **Runs inside an isolated Docker container**.
- Uses **Pyodide (WebAssembly) or Jailed Python VM** to prevent security risks.
- **Timeouts and memory limits** to avoid infinite loops.

---

## **7. Hosting & Deployment**
| Component  | Service |
|------------|----------|
| **Frontend (React + Code Editor + Vis.js/D3.js)** | Vercel or Netlify |
| **Backend (FastAPI + Execution Sandbox)** | Render, Fly.io, or Railway |
| **Database (Supabase)** | Stores graphs and user algorithms |
| **Execution Environment (Docker, Pyodide, or Jailed VM)** | Runs user-submitted code safely |

---

## **8. Additional Features (Future Enhancements)**
- **Real-Time Collaboration** (WebSockets for multi-user editing).
- **Graph Exporting** (SVG, JSON, GraphML).
- **Graph Animation Controls** (Playback speed, step-by-step visualization).
- **User Authentication & Profiles** (Save private/public graphs).
- **Leaderboard for Algorithm Efficiency** (Rank based on execution speed/memory usage).

---

## **9. Next Steps**
Would you like:
1. A **proof of concept** for user-submitted functions?
2. A **backend prototype** with a working API?
3. A **frontend UI wireframe** for the interactive graph editor?

