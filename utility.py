def in_line(coords):
    a, b = coords
    a = (a * 20)
    b = (b * 20)
    return a, b
    for c_vert in current_vertex:
        for g_vert in goal_vertex:
            if c_vert[3] == 1:
                vertex_scores[f"{c_vert[0]}{g_vert[0]}"] = 0
            else:
                vertex_scores[f"{c_vert[0]}{g_vert[0]}"] = sqrt((g_vert[1] - c_vert[1]) ** 2 + (g_vert[2] - c_vert[2]) ** 2)
