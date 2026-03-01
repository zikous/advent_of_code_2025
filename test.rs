#[derive(Debug)]
enum IterTree<'a, T: Clone> {
    Leaf(&'a [T]),
    Product(Vec<IterTree<'a, T>>),
    Zip(Vec<IterTree<'a, T>>),
}

/// Fully lazy iterator for nested Zip + Product
struct TreeIter<'a, T: Clone> {
    tree: &'a IterTree<'a, T>,
    stack: Vec<usize>, // current indices for leaves
    done: bool,
}

impl<'a, T: Clone> TreeIter<'a, T> {
    fn new(tree: &'a IterTree<'a, T>) -> Self {
        Self {
            tree,
            stack: Vec::new(),
            done: false,
        }
    }

    fn next_combination(&mut self) -> Option<Vec<T>> {
        if self.done {
            return None;
        }

        let mut combination = Vec::new();
        if !Self::build_combination(self.tree, &mut self.stack, &mut combination) {
            self.done = true;
            return None;
        }

        Self::advance_stack(&mut self.stack);
        Some(combination)
    }

    // Recursively build one combination from current indices
    fn build_combination(tree: &IterTree<'a, T>, stack: &mut Vec<usize>, out: &mut Vec<T>) -> bool {
        match tree {
            IterTree::Leaf(slice) => {
                let idx = if stack.len() < 1 {
                    stack.push(0);
                    0
                } else {
                    stack[stack.len() - 1]
                };
                if idx >= slice.len() {
                    return false;
                }
                out.push(slice[idx].clone());
                true
            }
            IterTree::Product(children) => {
                for (i, child) in children.iter().enumerate() {
                    if stack.len() <= i {
                        stack.push(0);
                    }
                    if !Self::build_combination(child, stack, out) {
                        return false;
                    }
                }
                true
            }
            IterTree::Zip(children) => {
                let min_len = children
                    .iter()
                    .map(|c| match c {
                        IterTree::Leaf(s) => s.len(),
                        IterTree::Product(_) | IterTree::Zip(_) => usize::MAX,
                    })
                    .min()
                    .unwrap_or(0);
                if stack.len() < 1 {
                    stack.push(0);
                }
                if stack[stack.len() - 1] >= min_len {
                    return false;
                }
                for child in children.iter() {
                    if !Self::build_combination(child, stack, out) {
                        return false;
                    }
                }
                true
            }
        }
    }

    // Increment indices for next combination
    fn advance_stack(stack: &mut Vec<usize>) {
        if !stack.is_empty() {
            *stack.last_mut().unwrap() += 1;
        }
    }
}

impl<'a, T: Clone> Iterator for TreeIter<'a, T> {
    type Item = Vec<T>;
    fn next(&mut self) -> Option<Self::Item> {
        self.next_combination()
    }
}

fn main() {
    let a = vec![1, 2];
    let b = vec![10, 20];
    let c = vec![100, 200];
    let d = vec![1000, 2000];
    let e = vec![5, 6];

    let tree = IterTree::Zip(vec![
        IterTree::Product(vec![IterTree::Leaf(&a), IterTree::Leaf(&b)]),
        IterTree::Zip(vec![IterTree::Leaf(&c), IterTree::Leaf(&d)]),
        IterTree::Leaf(&e),
    ]);

    for combo in TreeIter::new(&tree) {
        println!("{:?}", combo);
    }
}
