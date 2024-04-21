// Springy.Graphオブジェクトを作成する
var graph = new Springy.Graph();

// ノードを追加する
graph.addNodes([
  { id: 'n0', label: 'Node 0' },
  { id: 'n1', label: 'Node 1' },
  { id: 'n2', label: 'Node 2' },
  { id: 'n3', label: 'Node 3' }
]);

// エッジを追加する
graph.addEdges([
  { source: 'n0', target: 'n1' },
  { source: 'n1', target: 'n2' },
  { source: 'n2', target: 'n3' }
]);

// 描画する
var renderer = new Springy.Renderer(
  graph,
  function clear() {},
  function drawEdge(edge, p1, p2) {},
  function drawNode(node, p) {
    var pos = transformToScreen(p);
    node.data.ui.style.left = pos.x + 'px';
    node.data.ui.style.top = pos.y + 'px';
  }
);
renderer.start();
