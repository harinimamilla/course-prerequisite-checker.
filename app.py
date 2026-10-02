from flask import Flask, render_template_string, request, jsonify

app = Flask(__name__)

# ============================================================
# COURSE PREREQUISITE DIRECTED GRAPH
# ============================================================

graph = {
    "Programming Fundamentals": [],
    "Data Structures": ["Programming Fundamentals"],
    "Algorithms": ["Data Structures"],
    "Database Management": ["Programming Fundamentals"],
    "Web Development": ["Programming Fundamentals"],
    "Operating Systems": ["Data Structures"],
    "Computer Networks": ["Operating Systems"],
    "Python Programming": [],
    "Statistics": [],
    "Machine Learning": ["Python Programming", "Statistics"]
}


# ============================================================
# WEBSITE
# ============================================================

HTML = """

<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">

<meta name="viewport"
      content="width=device-width, initial-scale=1.0">

<title>CoursePath | Prerequisite Intelligence</title>

<style>

/* =========================================================
   GLOBAL
========================================================= */

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    font-family:
        "Segoe UI",
        Arial,
        sans-serif;

    background: #f5f7fb;

    color: #172033;
}

a {
    text-decoration: none;
    color: inherit;
}

button,
select {
    font-family: inherit;
}


/* =========================================================
   SIDEBAR
========================================================= */

.sidebar {

    position: fixed;

    left: 0;
    top: 0;

    width: 250px;
    height: 100vh;

    background:
        linear-gradient(
            180deg,
            #07162f,
            #0b2347,
            #102f59
        );

    color: white;

    padding: 28px 18px;

    z-index: 1000;

    box-shadow:
        8px 0 30px rgba(0,0,0,0.08);
}

.logo {

    display: flex;

    align-items: center;

    gap: 12px;

    padding: 0 12px;

    margin-bottom: 45px;
}

.logo-icon {

    width: 44px;
    height: 44px;

    border-radius: 13px;

    display: flex;
    align-items: center;
    justify-content: center;

    background:
        linear-gradient(
            135deg,
            #4f9cff,
            #7b61ff
        );

    font-size: 22px;

    box-shadow:
        0 8px 20px rgba(79,156,255,.25);
}

.logo h2 {
    font-size: 20px;
}

.logo span {
    display: block;

    color: #91a8ca;

    font-size: 11px;

    margin-top: 2px;
}

.menu-title {

    font-size: 11px;

    color: #6f87aa;

    letter-spacing: 1.5px;

    padding: 0 14px;

    margin-bottom: 12px;
}

.nav {

    display: flex;

    flex-direction: column;

    gap: 7px;
}

.nav a {

    padding: 13px 15px;

    border-radius: 12px;

    color: #aebed6;

    display: flex;

    align-items: center;

    gap: 12px;

    transition: .25s;
}

.nav a:hover {

    background:
        rgba(255,255,255,.08);

    color: white;

    transform: translateX(3px);
}

.nav a.active {

    background:
        linear-gradient(
            135deg,
            #2867c7,
            #174d9d
        );

    color: white;

    box-shadow:
        0 8px 20px rgba(18,86,177,.25);
}

.nav-icon {
    width: 25px;
    text-align: center;
}


/* =========================================================
   SIDEBAR BOTTOM
========================================================= */

.sidebar-bottom {

    position: absolute;

    bottom: 25px;

    left: 18px;
    right: 18px;

    padding: 17px;

    border-radius: 14px;

    background:
        rgba(255,255,255,.06);

    border:
        1px solid rgba(255,255,255,.08);
}

.sidebar-bottom p {

    font-size: 11px;

    color: #7e96b8;

    margin-bottom: 5px;
}

.sidebar-bottom strong {

    font-size: 13px;
}


/* =========================================================
   MAIN
========================================================= */

.main {

    margin-left: 250px;

    min-height: 100vh;

    padding: 28px 42px 50px;
}


/* =========================================================
   TOPBAR
========================================================= */

.topbar {

    display: flex;

    justify-content: space-between;

    align-items: center;

    margin-bottom: 30px;
}

.breadcrumb {

    color: #8390a5;

    font-size: 13px;
}

.breadcrumb strong {

    color: #26344d;
}

.status {

    display: flex;

    align-items: center;

    gap: 8px;

    padding: 8px 14px;

    background: white;

    border-radius: 30px;

    font-size: 12px;

    box-shadow:
        0 4px 15px rgba(0,0,0,.05);
}

.status-dot {

    width: 8px;
    height: 8px;

    border-radius: 50%;

    background: #22c55e;

    box-shadow:
        0 0 0 4px rgba(34,197,94,.12);
}


/* =========================================================
   HERO
========================================================= */

.hero {

    position: relative;

    overflow: hidden;

    padding: 45px;

    border-radius: 25px;

    color: white;

    background:
        linear-gradient(
            120deg,
            #071a38,
            #123d78,
            #246bc0
        );

    box-shadow:
        0 18px 40px rgba(16,60,120,.18);

    margin-bottom: 28px;
}

.hero::before {

    content: "";

    position: absolute;

    width: 300px;
    height: 300px;

    border-radius: 50%;

    right: -80px;
    top: -120px;

    background:
        rgba(255,255,255,.07);
}

.hero::after {

    content: "";

    position: absolute;

    width: 180px;
    height: 180px;

    border-radius: 50%;

    right: 150px;
    bottom: -120px;

    background:
        rgba(255,255,255,.05);
}

.hero-content {

    position: relative;

    z-index: 2;

    max-width: 720px;
}

.badge {

    display: inline-block;

    padding: 7px 13px;

    border-radius: 30px;

    background:
        rgba(255,255,255,.12);

    border:
        1px solid rgba(255,255,255,.15);

    font-size: 11px;

    letter-spacing: .5px;

    margin-bottom: 18px;
}

.hero h1 {

    font-size: 39px;

    line-height: 1.15;

    margin-bottom: 15px;
}

.hero p {

    color: #c8d8ef;

    line-height: 1.7;

    max-width: 650px;

    font-size: 15px;
}

.hero-buttons {

    margin-top: 25px;

    display: flex;

    gap: 12px;

    flex-wrap: wrap;
}

.hero-btn {

    padding: 12px 18px;

    border-radius: 10px;

    background: white;

    color: #174d9d;

    font-weight: 600;

    font-size: 13px;

    border: none;

    cursor: pointer;

    transition: .2s;
}

.hero-btn:hover {
    transform: translateY(-2px);
}

.hero-btn.secondary {

    background:
        rgba(255,255,255,.1);

    color: white;

    border:
        1px solid rgba(255,255,255,.2);
}


/* =========================================================
   SECTION TITLE
========================================================= */

.section-title {

    display: flex;

    justify-content: space-between;

    align-items: center;

    margin: 32px 0 17px;
}

.section-title h2 {

    font-size: 20px;

    color: #172b4d;
}

.section-title span {

    color: #8995a8;

    font-size: 12px;
}


/* =========================================================
   STATS
========================================================= */

.stats {

    display: grid;

    grid-template-columns:
        repeat(4, 1fr);

    gap: 17px;
}

.stat-card {

    background: white;

    border-radius: 17px;

    padding: 21px;

    display: flex;

    align-items: center;

    gap: 15px;

    box-shadow:
        0 7px 24px rgba(25,45,80,.06);

    border:
        1px solid #edf0f5;

    transition: .25s;
}

.stat-card:hover {

    transform: translateY(-4px);

    box-shadow:
        0 14px 30px rgba(25,45,80,.1);
}

.stat-icon {

    width: 48px;
    height: 48px;

    border-radius: 13px;

    display: flex;

    align-items: center;

    justify-content: center;

    font-size: 20px;

    background: #edf4ff;
}

.stat-card h3 {

    font-size: 22px;

    color: #172b4d;
}

.stat-card p {

    color: #8a95a7;

    font-size: 11px;

    margin-top: 3px;
}


/* =========================================================
   CHECKER AREA
========================================================= */

.checker-grid {

    display: grid;

    grid-template-columns:
        1.35fr .65fr;

    gap: 20px;
}

.panel {

    background: white;

    border-radius: 19px;

    padding: 26px;

    border:
        1px solid #edf0f5;

    box-shadow:
        0 7px 24px rgba(25,45,80,.06);
}

.panel-head {

    display: flex;

    justify-content: space-between;

    align-items: center;

    margin-bottom: 22px;
}

.panel-head h3 {

    font-size: 17px;

    color: #172b4d;
}

.panel-head span {

    font-size: 11px;

    color: #8290a5;
}


/* =========================================================
   SELECT
========================================================= */

label.main-label {

    display: block;

    font-size: 12px;

    font-weight: 700;

    color: #506079;

    margin-bottom: 8px;
}

select {

    width: 100%;

    padding: 13px 14px;

    border:
        1px solid #dce2ea;

    border-radius: 10px;

    background: #fbfcfe;

    color: #27364d;

    outline: none;

    cursor: pointer;

    margin-bottom: 16px;
}

select:focus {

    border-color: #3276d1;

    box-shadow:
        0 0 0 3px rgba(50,118,209,.1);
}


/* =========================================================
   PREREQUISITE BOX
========================================================= */

.prerequisite {

    padding: 16px;

    border-radius: 13px;

    background:
        linear-gradient(
            135deg,
            #f0f6ff,
            #f8fbff
        );

    border:
        1px solid #dceaff;

    margin-bottom: 20px;
}

.prerequisite-title {

    color: #1958a6;

    font-size: 12px;

    font-weight: 700;

    margin-bottom: 9px;
}

.prerequisite-item {

    display: inline-block;

    padding: 6px 10px;

    background: white;

    border-radius: 7px;

    margin: 3px;

    font-size: 11px;

    color: #52647d;

    border:
        1px solid #e1eaf7;
}


/* =========================================================
   COURSE CHECKBOXES
========================================================= */

.course-grid {

    display: grid;

    grid-template-columns:
        repeat(2, 1fr);

    gap: 9px;

    max-height: 300px;

    overflow-y: auto;

    padding-right: 4px;
}

.course-option {

    position: relative;

    cursor: pointer;
}

.course-option input {

    position: absolute;

    opacity: 0;
}

.course-label {

    display: block;

    padding: 12px;

    border:
        1px solid #e4e8ef;

    border-radius: 10px;

    font-size: 11px;

    color: #58677d;

    transition: .2s;

    background: #fcfdff;
}

.course-option input:checked
+ .course-label {

    background: #edf5ff;

    border-color: #5c94d8;

    color: #1557a6;

    font-weight: 700;
}


/* =========================================================
   BUTTON
========================================================= */

.check-btn {

    width: 100%;

    margin-top: 20px;

    padding: 14px;

    border: none;

    border-radius: 11px;

    color: white;

    font-weight: 700;

    cursor: pointer;

    background:
        linear-gradient(
            135deg,
            #1764c0,
            #3788e3
        );

    box-shadow:
        0 8px 18px rgba(23,100,192,.2);

    transition: .25s;
}

.check-btn:hover {

    transform: translateY(-2px);

    box-shadow:
        0 12px 25px rgba(23,100,192,.25);
}


/* =========================================================
   RESULT
========================================================= */

.result {

    margin-top: 17px;

    padding: 17px;

    border-radius: 12px;

    display: none;

    font-size: 12px;

    line-height: 1.7;
}

.result.success {

    display: block;

    background: #ecfdf3;

    border:
        1px solid #b8ebce;

    color: #14713d;
}

.result.error {

    display: block;

    background: #fff3f3;

    border:
        1px solid #f0c5c5;

    color: #a53131;
}


/* =========================================================
   GRAPH VISUALIZATION
========================================================= */

.graph-box {

    background:
        linear-gradient(
            135deg,
            #081a35,
            #123c72
        );

    border-radius: 17px;

    padding: 25px;

    color: white;

    min-height: 100%;
}

.graph-box h3 {

    font-size: 17px;

    margin-bottom: 5px;
}

.graph-box > p {

    font-size: 11px;

    color: #a9bedc;

    margin-bottom: 25px;
}

.flow {

    display: flex;

    flex-direction: column;

    gap: 10px;
}

.node {

    padding: 12px 14px;

    border-radius: 10px;

    background:
        rgba(255,255,255,.08);

    border:
        1px solid rgba(255,255,255,.1);

    font-size: 11px;

    transition: .2s;
}

.node:hover {

    background:
        rgba(255,255,255,.14);

    transform: translateX(4px);
}

.arrow {

    text-align: center;

    color: #6fa8ef;

    font-size: 14px;
}


/* =========================================================
   COURSE DIRECTORY
========================================================= */

.course-cards {

    display: grid;

    grid-template-columns:
        repeat(3, 1fr);

    gap: 14px;
}

.course-card {

    background: white;

    border-radius: 15px;

    padding: 18px;

    border:
        1px solid #edf0f5;

    transition: .25s;
}

.course-card:hover {

    transform: translateY(-4px);

    border-color: #cbdcf4;

    box-shadow:
        0 12px 28px rgba(25,45,80,.08);
}

.course-number {

    width: 31px;
    height: 31px;

    border-radius: 9px;

    background: #edf4ff;

    color: #1b5ba9;

    display: flex;

    align-items: center;

    justify-content: center;

    font-size: 11px;

    font-weight: 700;

    margin-bottom: 12px;
}

.course-card h4 {

    font-size: 13px;

    margin-bottom: 7px;

    color: #253651;
}

.course-card p {

    font-size: 10px;

    color: #8a96a8;

    line-height: 1.5;
}


/* =========================================================
   HOW IT WORKS
========================================================= */

.steps {

    display: grid;

    grid-template-columns:
        repeat(4, 1fr);

    gap: 15px;
}

.step {

    padding: 20px;

    background: white;

    border-radius: 15px;

    border:
        1px solid #edf0f5;

    text-align: center;
}

.step-number {

    width: 35px;
    height: 35px;

    border-radius: 50%;

    background: #edf4ff;

    color: #185cae;

    display: flex;

    align-items: center;

    justify-content: center;

    margin: 0 auto 12px;

    font-size: 12px;

    font-weight: 700;
}

.step h4 {

    font-size: 13px;

    margin-bottom: 6px;
}

.step p {

    font-size: 10px;

    color: #8792a4;

    line-height: 1.5;
}


/* =========================================================
   FOOTER
========================================================= */

footer {

    margin-top: 40px;

    padding-top: 25px;

    border-top:
        1px solid #e3e7ee;

    text-align: center;

    color: #8a95a7;

    font-size: 11px;
}


/* =========================================================
   RESPONSIVE
========================================================= */

@media(max-width:1100px) {

    .stats {
        grid-template-columns:
            repeat(2, 1fr);
    }

    .checker-grid {
        grid-template-columns: 1fr;
    }

    .course-cards {
        grid-template-columns:
            repeat(2, 1fr);
    }

    .steps {
        grid-template-columns:
            repeat(2, 1fr);
    }
}

@media(max-width:750px) {

    .sidebar {

        position: relative;

        width: 100%;

        height: auto;

        padding: 18px;

    }

    .sidebar-bottom {
        display: none;
    }

    .logo {
        margin-bottom: 20px;
    }

    .nav {
        flex-direction: row;
        flex-wrap: wrap;
    }

    .nav a {
        font-size: 11px;
    }

    .main {

        margin-left: 0;

        padding: 20px;
    }

    .hero {
        padding: 28px;
    }

    .hero h1 {
        font-size: 28px;
    }

    .stats {
        grid-template-columns: 1fr;
    }

    .course-cards {
        grid-template-columns: 1fr;
    }

    .steps {
        grid-template-columns: 1fr;
    }

    .course-grid {
        grid-template-columns: 1fr;
    }
}

</style>

</head>


<body>


<!-- =====================================================
     SIDEBAR
===================================================== -->

<aside class="sidebar">

    <div class="logo">

        <div class="logo-icon">
            CP
        </div>

        <div>

            <h2>CoursePath</h2>

            <span>Academic Intelligence</span>

        </div>

    </div>


    <div class="menu-title">
        MAIN MENU
    </div>


    <nav class="nav">

        <a href="#dashboard" class="active">
            <span class="nav-icon">⌂</span>
            Dashboard
        </a>

        <a href="#checker">
            <span class="nav-icon">✓</span>
            Course Checker
        </a>

        <a href="#courses">
            <span class="nav-icon">▦</span>
            Course Directory
        </a>

        <a href="#graph">
            <span class="nav-icon">◇</span>
            Graph Structure
        </a>

        <a href="#about">
            <span class="nav-icon">ⓘ</span>
            About Project
        </a>

    </nav>


    <div class="sidebar-bottom">

        <p>PROJECT TYPE</p>

        <strong>Directed Graph Application</strong>

    </div>

</aside>



<!-- =====================================================
     MAIN CONTENT
===================================================== -->

<main class="main">


    <!-- TOP BAR -->

    <div class="topbar">

        <div class="breadcrumb">

            CoursePath
            /
            <strong>Dashboard</strong>

        </div>


        <div class="status">

            <span class="status-dot"></span>

            System Online

        </div>

    </div>



    <!-- HERO -->

    <section class="hero" id="dashboard">

        <div class="hero-content">

            <span class="badge">
                DIRECTED GRAPH • ACADEMIC PLANNING
            </span>


            <h1>
                Plan your next course
                with confidence.
            </h1>


            <p>

                CoursePath analyzes prerequisite
                relationships between courses using
                a directed graph and helps students
                understand their course eligibility.

            </p>


            <div class="hero-buttons">

                <a
                    href="#checker"
                    class="hero-btn"
                >
                    Check Eligibility →
                </a>

                <a
                    href="#graph"
                    class="hero-btn secondary"
                >
                    Explore Graph
                </a>

            </div>

        </div>

    </section>



    <!-- STATISTICS -->

    <div class="section-title">

        <h2>System Overview</h2>

        <span>Live project data</span>

    </div>


    <section class="stats">

        <div class="stat-card">

            <div class="stat-icon">
                🎓
            </div>

            <div>

                <h3>{{ total_courses }}</h3>

                <p>Total Courses</p>

            </div>

        </div>


        <div class="stat-card">

            <div class="stat-icon">
                🔗
            </div>

            <div>

                <h3>9+</h3>

                <p>Prerequisite Links</p>

            </div>

        </div>


        <div class="stat-card">

            <div class="stat-icon">
                🧠
            </div>

            <div>

                <h3>Graph</h3>
                <p>Core Data Structure</p>

            </div>

        </div>


        <div class="stat-card">

            <div class="stat-icon">
                ⚡
            </div>

            <div>

                <h3>Flask</h3>

                <p>Backend Framework</p>

            </div>

        </div>

    </section>



    <!-- CHECKER -->

    <div
        class="section-title"
        id="checker"
    >

        <h2>Course Eligibility Checker</h2>

        <span>Analyze prerequisites</span>

    </div>


    <section class="checker-grid">


        <!-- LEFT -->

        <div class="panel">

            <div class="panel-head">

                <h3>
                    Check Course Requirements
                </h3>

                <span>
                    Step-by-step analysis
                </span>

            </div>


            <label class="main-label">

                Target Course

            </label>


            <select
                id="targetCourse"
                onchange="showPrerequisites()"
            >

                <option value="">
                    Select the course you want to take
                </option>

                {% for course in courses %}

                <option value="{{ course }}">
                    {{ course }}
                </option>

                {% endfor %}

            </select>


            <div
                id="prerequisiteBox"
                class="prerequisite"
                style="display:none;"
            >

                <div class="prerequisite-title">

                    🔗 Required Prerequisites

                </div>

                <div id="requiredList"></div>

            </div>


            <label class="main-label">

                Courses Already Completed

            </label>


            <div class="course-grid">

                {% for course in courses %}

                <label class="course-option">

                    <input
                        type="checkbox"
                        class="completed"
                        value="{{ course }}"
                        onchange="updateCount()"
                    >

                    <span class="course-label">

                        {{ course }}

                    </span>

                </label>

                {% endfor %}

            </div>


            <button
                class="check-btn"
                onclick="checkEligibility()"
            >

                Analyse Eligibility →

            </button>


            <div
                id="result"
                class="result"
            ></div>

        </div>



        <!-- RIGHT -->

        <div
            class="graph-box"
            id="graph"
        >

            <h3>
                Prerequisite Flow
            </h3>

            <p>
                Example of directed course dependency
            </p>


            <div class="flow">

                <div class="node">
                    Programming Fundamentals
                </div>

                <div class="arrow">↓</div>

                <div class="node">
                    Data Structures
                </div>

                <div class="arrow">↓</div>

                <div class="node">
                    Algorithms
                </div>

                <div class="arrow">↓</div>

                <div class="node">
                    Advanced Computer Courses
                </div>

            </div>


            <div style="
                margin-top:25px;
                padding:15px;
                border-radius:11px;
                background:rgba(255,255,255,.06);
                font-size:11px;
                line-height:1.7;
                color:#b8cae3;
            ">

                <strong style="color:white;">
                    Graph Concept
                </strong>

                <br><br>

                A → B means course A is a
                prerequisite for course B.

            </div>

        </div>

    </section>



    <!-- COURSE DIRECTORY -->

    <div
        class="section-title"
        id="courses"
    >

        <h2>Course Directory</h2>

        <span>
            {{ total_courses }} available courses
        </span>

    </div>


    <section class="course-cards">

        {% for course in courses %}

        <div class="course-card">

            <div class="course-number">

                {{ "%02d" | format(loop.index) }}

            </div>


            <h4>
                {{ course }}
            </h4>


            {% if graph[course] %}

            <p>
                Requires:
                {{ graph[course] | join(", ") }}
            </p>

            {% else %}

            <p>
                No prerequisite required.
            </p>

            {% endif %}

        </div>

        {% endfor %}

    </section>



    <!-- HOW IT WORKS -->

    <div class="section-title">

        <h2>How the System Works</h2>

        <span>Simple four-step process</span>

    </div>


    <section class="steps">

        <div class="step">

            <div class="step-number">
                01
            </div>

            <h4>
                Select Course
            </h4>

            <p>
                Choose the course you
                want to study.
            </p>

        </div>


        <div class="step">

            <div class="step-number">
                02
            </div>

            <h4>
                Select Completed
            </h4>

            <p>
                Mark the courses you
                have already completed.
            </p>

        </div>


        <div class="step">

            <div class="step-number">
                03
            </div>

            <h4>
                Analyse Graph
            </h4>

            <p>
                The system compares
                prerequisites with your
                completed courses.
            </p>

        </div>


        <div class="step">

            <div class="step-number">
                04
            </div>

            <h4>
                Get Result
            </h4>

            <p>
                View your eligibility and
                missing prerequisites.
            </p>

        </div>

    </section>



    <!-- ABOUT -->

    <div
        class="section-title"
        id="about"
    >

        <h2>About the Project</h2>

        <span>Academic project</span>

    </div>


    <section class="panel">

        <p style="
            font-size:13px;
            line-height:1.9;
            color:#69778d;
        ">

            <strong style="color:#1b4f91;">
                Course Prerequisite Checker Using Directed Graph
            </strong>

            is a full-stack academic project designed
            to represent course prerequisite relationships
            using a directed graph.

            Each course is represented as a node and each
            prerequisite relationship is represented as a
            directed edge.

            The system uses

            <strong>HTML, CSS, JavaScript and Python Flask</strong>

            to provide an interactive platform for checking
            course eligibility.

        </p>

    </section>



    <!-- FOOTER -->

    <footer>

        CoursePath • Course Prerequisite Checker

        <br><br>

        Built using Directed Graph + Python Flask

    </footer>


</main>



<script>


// ========================================================
// GRAPH DATA FROM FLASK
// ========================================================

const graph = {{ graph | tojson }};


// ========================================================
// SHOW PREREQUISITES
// ========================================================

function showPrerequisites() {

    const course =
        document.getElementById("targetCourse").value;

    const box =
        document.getElementById("prerequisiteBox");

    const list =
        document.getElementById("requiredList");


    if (!course) {

        box.style.display = "none";

        return;

    }


    box.style.display = "block";


    const prerequisites =
        graph[course];


    if (
        !prerequisites ||
        prerequisites.length === 0
    ) {

        list.innerHTML =
            '<span class="prerequisite-item">' +
            'No prerequisites required' +
            '</span>';

        return;

    }


    list.innerHTML =
        prerequisites
        .map(function(item) {

            return (
                '<span class="prerequisite-item">' +
                item +
                '</span>'
            );

        })
        .join("");

}


// ========================================================
// CHECK ELIGIBILITY
// ========================================================

async function checkEligibility() {

    const course =
        document.getElementById("targetCourse").value;


    const result =
        document.getElementById("result");


    if (!course) {

        result.className =
            "result error";

        result.style.display =
            "block";

        result.innerHTML =
            "⚠ Please select a target course first.";

        return;

    }


    const completed = [];


    document
        .querySelectorAll(".completed:checked")
        .forEach(function(box) {

            completed.push(box.value);

        });


    try {

        const response =
            await fetch("/check", {

                method: "POST",

                headers: {

                    "Content-Type":
                        "application/json"

                },

                body: JSON.stringify({

                    course: course,

                    completed: completed

                })

            });


        const data =
            await response.json();


        if (data.eligible) {

            result.className =
                "result success";

            result.style.display =
                "block";

            result.innerHTML =

                "<strong>✓ Eligible</strong><br>" +

                "You have completed all required " +

                "prerequisites for <strong>" +

                course +

                "</strong>.";

        }

        else {

            result.className =
                "result error";

            result.style.display =
                "block";


            let missing =
                data.missing
                .map(function(item) {

                    return "<li>" + item + "</li>";

                })
                .join("");


            result.innerHTML =

                "<strong>✕ Not Eligible</strong><br>" +

                "The following prerequisite(s) " +

                "are still required:" +

                "<ul style='margin-top:8px;margin-left:18px;'>" +

                missing +

                "</ul>";

        }


    }

    catch(error) {

        result.className =
            "result error";

        result.style.display =
            "block";

        result.innerHTML =
            "⚠ Unable to connect to the Flask server.";

    }

}

</script>


</body>

</html>

"""


# ============================================================
# HOME
# ============================================================

@app.route("/")
def home():

    return render_template_string(

        HTML,

        courses=list(graph.keys()),

        graph=graph,

        total_courses=len(graph)

    )


# ============================================================
# CHECK API
# ============================================================

@app.route("/check", methods=["POST"])
def check():

    data = request.get_json()

    course = data.get("course")

    completed = data.get("completed", [])


    if course not in graph:

        return jsonify({

            "eligible": False,

            "missing": [],

            "message": "Course not found"

        })


    missing = []


    for prerequisite in graph[course]:

        if prerequisite not in completed:

            missing.append(prerequisite)


    if len(missing) == 0:

        return jsonify({

            "eligible": True,

            "missing": []

        })


    return jsonify({

        "eligible": False,

        "missing": missing

    })


# ============================================================
# START SERVER
# ============================================================

if __name__ == "__main__":

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )

""