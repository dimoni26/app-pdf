import styles from '../styles/layout.module.css'

export default function Layout(props) {
  return (
    <div className={styles.layout}>
      <h1 className={styles.title}>Basic PDF CRUD App</h1>
      <p className={styles.subtitle}>Hecho por <a href="www.autmatix.es" target="_blank">Autmatix</a> y <a href="www.autmatix.es" target="_blank">Dimoni</a></p>
      {props.children}
    </div>
  )
}