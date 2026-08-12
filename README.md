<h1>Escape Room Solver</h1>

<p>
  Escape Room Solver is a stateful LLM-powered workflow that solves an escape room by
  analyzing clues, selecting actions, tracking inventory and observations, and repeatedly
  updating the room state until the puzzle is solved.
</p>

<h2>Overview</h2>

<p>
  The project demonstrates how <strong>LangChain</strong> and <strong>LangGraph</strong>
  can be used to build a stateful workflow rather than a simple one-shot LLM application.
  The solver maintains a shared state throughout the game and uses the LLM to determine
  the next action based on the clues and information discovered so far.
</p>

<p>
  The workflow continues until the room is successfully solved.
</p>

<h2>How It Works</h2>

<pre>
Initial Room State
       |
       v
 Analyze Room
       |
       v
 Choose Next Action
       |
       v
 Execute Action
       |
       v
 Update State
       |
       v
 Check if Solved
    /        \
  No          Yes
  |            |
  v            v
Analyze       End
Again
</pre>

<p>
  The solver uses a conditional loop in LangGraph. If the room is not solved,
  the updated state is passed back to the analysis node. If the room is solved,
  the workflow terminates.
</p>

<h2>Example</h2>

<p>
  The example escape room contains a locked study, a stopped clock, a keypad drawer,
  and a locked main door.
</p>

<p>
  The solver first identifies that the clock is stopped at <strong>3:15</strong> and
  reasons that <strong>315</strong> may be the code for the drawer.
</p>

<p>
  After entering the code, the drawer opens and a silver key is discovered.
  The inventory is updated with the new key and the solver continues reasoning.
</p>

<p>
  The solver then determines that the silver key can be used on the main door.
  After the door is unlocked, the workflow marks the room as solved and terminates.
</p>

<h2>Key Features</h2>

<ul>
  <li>Stateful escape room solving using LangGraph</li>
  <li>LLM-based clue analysis and action selection</li>
  <li>Structured LLM responses using Pydantic</li>
  <li>Clue tracking throughout the workflow</li>
  <li>Inventory tracking</li>
  <li>Observation and action history</li>
  <li>Conditional workflow routing</li>
  <li>Iterative reasoning until the puzzle is solved</li>
</ul>

<h2>Workflow State</h2>

<p>
  The workflow maintains a shared state throughout the solving process.
</p>

<table>
  <thead>
    <tr>
      <th>State</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>room_state</code></td>
      <td>Current description of the escape room.</td>
    </tr>
    <tr>
      <td><code>clues</code></td>
      <td>Clues discovered during the solving process.</td>
    </tr>
    <tr>
      <td><code>inventory</code></td>
      <td>Items currently available to the solver.</td>
    </tr>
    <tr>
      <td><code>observations</code></td>
      <td>Results and information gathered from previous actions.</td>
    </tr>
    <tr>
      <td><code>current_action</code></td>
      <td>The next action selected by the LLM.</td>
    </tr>
    <tr>
      <td><code>action_result</code></td>
      <td>The result produced after executing the selected action.</td>
    </tr>
    <tr>
      <td><code>solution</code></td>
      <td>The final solution once the room has been solved.</td>
    </tr>
    <tr>
      <td><code>is_solved</code></td>
      <td>Indicates whether the escape room has been solved.</td>
    </tr>
  </tbody>
</table>

<h2>LangGraph Workflow</h2>

<p>
  The workflow is composed of three main nodes:
</p>

<h3>1. Analyze Room</h3>

<p>
  The LLM analyzes the current room state, clues, inventory, observations,
  and previous actions. It produces a structured decision containing the
  next action, new clues, observations, and solved status.
</p>

<h3>2. Execute Action</h3>

<p>
  The selected action is passed to the simulated escape room environment.
  The environment determines what happens as a result of the action and
  updates the inventory, clues, and observations.
</p>

<h3>3. Check Solved</h3>

<p>
  The workflow checks whether the latest action solved the room. If the room
  is not solved, LangGraph routes the state back to the analysis node.
  If the room is solved, the workflow terminates.
</p>

<h2>Project Structure</h2>

<pre>
EscapeRoomSolver/
|
├── app/
│   ├── __init__.py
│   ├── state.py
│   ├── llm.py
│   ├── prompts.py
│   ├── nodes.py
│   └── graph.py
|
├── main.py
├── requirements.txt
├── .env
└── .gitignore
</pre>

<h2>File Description</h2>

<table>
  <thead>
    <tr>
      <th>File</th>
      <th>Purpose</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>state.py</code></td>
      <td>Defines the shared LangGraph workflow state.</td>
    </tr>
    <tr>
      <td><code>llm.py</code></td>
      <td>Configures the Groq LLM and structured output schema.</td>
    </tr>
    <tr>
      <td><code>prompts.py</code></td>
      <td>Contains the instructions used by the escape room solver.</td>
    </tr>
    <tr>
      <td><code>nodes.py</code></td>
      <td>Contains the workflow nodes for analysis, action execution, and solving checks.</td>
    </tr>
    <tr>
      <td><code>graph.py</code></td>
      <td>Builds and connects the LangGraph workflow.</td>
    </tr>
    <tr>
      <td><code>main.py</code></td>
      <td>Initializes the room and runs the workflow.</td>
    </tr>
  </tbody>
</table>

<h2>Tech Stack</h2>

<ul>
  <li>Python</li>
  <li>LangChain</li>
  <li>LangGraph</li>
  <li>Groq</li>
  <li>Llama 3.3 70B Versatile</li>
  <li>Pydantic</li>
  <li>python-dotenv</li>
</ul>

<h2>Installation</h2>

<h3>1. Clone the Repository</h3>

<pre>
git clone &lt;repository-url&gt;
cd EscapeRoomSolver
</pre>

<h3>2. Install Dependencies</h3>

<pre>
pip install -r requirements.txt
</pre>

<h3>3. Configure the API Key</h3>

<p>
  Create a <code>.env</code> file in the project root:
</p>

<pre>
GROQ_API_KEY=your_groq_api_key
</pre>

<h3>4. Run the Application</h3>

<pre>
python main.py
</pre>

<h2>Example Output</h2>

<pre>
===== ESCAPE ROOM SOLVER =====

Next Action:
Try entering 315 into the wooden drawer's keypad

Action Result:
The code 315 is correct. The wooden drawer opens.
Inside the drawer, you find a silver key.

Next Action:
Use the silver key to unlock the main door

Action Result:
You use the silver key on the main door. The door unlocks.
</pre>

<h2>Learning Objectives</h2>

<p>
  This project was built to understand the workflow-based approach to LLM
  application development using LangGraph.
</p>

<ul>
  <li>Understanding shared state in LangGraph</li>
  <li>Building sequential workflow nodes</li>
  <li>Using conditional edges for workflow routing</li>
  <li>Creating iterative LLM workflows</li>
  <li>Using structured LLM output</li>
  <li>Maintaining context across multiple reasoning steps</li>
  <li>Separating LLM reasoning from workflow control</li>
</ul>

<h2>Future Improvements</h2>

<ul>
  <li>Support multiple escape room configurations</li>
  <li>Add more complex puzzles and dependencies between clues</li>
  <li>Add failed-action tracking to prevent repeated actions</li>
  <li>Allow the solver to interact with a larger set of room objects</li>
  <li>Add persistent game state</li>
</ul>
