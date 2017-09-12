/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package imp;

import factory.NewHibernateUtil;
import org.hibernate.cfg.AnnotationConfiguration;
import org.hibernate.SessionFactory;
import java.sql.SQLException;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import javax.swing.JOptionPane;
import org.hibernate.Session;
import pojoclass.CatDAO;
import pojoclass.CatPOJO;

/**
 *
 * @author YURIES
 */
public class CatDAOImp implements CatDAO {

    @Override
    public void addCat(CatPOJO cat) throws SQLException {
        Session session = null;
        try {
            session = NewHibernateUtil.getSessionFactory().openSession();
            session.beginTransaction();
            session.save(cat);
            System.out.println("Saving object " + cat);
            session.getTransaction().commit();
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, e.getMessage(), "this", JOptionPane.OK_OPTION);
        } finally {
            if (session != null && session.isOpen()) {
                session.close();
            }
        }
    }

    @Override
    public void updateCat(Long cat_id, CatPOJO cat) throws SQLException {
        Session session = null;
        try {
            session = NewHibernateUtil.getSessionFactory().openSession();
            session.beginTransaction();
            session.update(cat);
            session.getTransaction().commit();
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, e.getMessage(), "this", JOptionPane.OK_OPTION);
        } finally {
            if (session != null && session.isOpen()) {
                session.close();
            }
        }
    }

    @Override
    public CatPOJO getCatById(Long id) throws SQLException {
        CatPOJO targetCat = null;
        Session session = null;
        try {
            session = NewHibernateUtil.getSessionFactory().openSession();
            targetCat = (CatPOJO) session.get(CatPOJO.class, id);
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, e.getMessage(), "this", JOptionPane.OK_OPTION);
        } finally {
            if (session != null && session.isOpen()) {
                session.close();
            }
        }
        return targetCat;
    }

    @Override
    public Collection getAllCats() throws SQLException {
        Session session = null;
        List busses = new ArrayList<CatPOJO>();
        try {
            session = NewHibernateUtil.getSessionFactory().openSession();
            busses = session.createCriteria(CatPOJO.class).list();
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, e.getMessage(), "Ошибка 'getAll'", JOptionPane.OK_OPTION);
        } finally {
            if (session != null && session.isOpen()) {
                session.close();
            }
        }
        return busses;
    }

    @Override
    public void deleteCat(CatPOJO bus) throws SQLException {
        Session session = null;
        try {
            session = NewHibernateUtil.getSessionFactory().openSession();
            session.beginTransaction();
            session.delete(bus);
            session.getTransaction().commit();

        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, e.getMessage(), "hrnei", JOptionPane.OK_OPTION);
        } finally {
            if (session != null && session.isOpen()) {
                session.close();
            }
        }
    }

    public void DeleteCatById(Long cat_id) throws SQLException {
        Session session = null;
        CatPOJO whtCatIsLookingFor = null;
        System.out.println("Was called with " + cat_id);
        try {
            session = NewHibernateUtil.getSessionFactory().openSession();
            whtCatIsLookingFor = (CatPOJO) session.load(CatPOJO.class, cat_id);
            session.delete(whtCatIsLookingFor);
            session.beginTransaction().commit();
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, e.getMessage(), "Crapp happend sometimes", JOptionPane.OK_OPTION);
        } finally {
            if (session != null && session.isOpen()) {
                session.close();
            }
        }

    }

}
